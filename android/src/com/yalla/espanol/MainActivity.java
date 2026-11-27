package com.yalla.espanol;

import android.app.Activity;
import android.content.Intent;
import android.net.ConnectivityManager;
import android.net.Network;
import android.net.NetworkCapabilities;
import android.net.Uri;
import android.os.Build;
import android.os.Bundle;
import android.view.View;
import android.view.ViewGroup;
import android.Manifest;
import android.content.pm.PackageManager;
import android.webkit.CookieManager;
import android.webkit.PermissionRequest;
import android.webkit.RenderProcessGoneDetail;
import android.webkit.WebChromeClient;
import android.webkit.MimeTypeMap;
import android.webkit.ServiceWorkerClient;
import android.webkit.ServiceWorkerController;
import android.webkit.WebResourceRequest;
import android.webkit.WebResourceResponse;
import android.webkit.WebSettings;
import android.webkit.WebView;
import android.webkit.WebViewClient;
import android.widget.FrameLayout;
import java.io.InputStream;
import java.util.HashMap;
import java.util.Map;

public class MainActivity extends Activity {
    static final String HOST = "yalla-espanol.pages.dev";
    static final String HOME = "https://" + HOST + "/";
    WebView web;
    PermissionRequest pending;
    String pendingCode;
    static final String PREFS = "yalla_auth";

    String newState() {
        byte[] r = new byte[16];
        new java.security.SecureRandom().nextBytes(r);
        StringBuilder sb = new StringBuilder();
        for (byte x : r) sb.append(String.format("%02x", x));
        getSharedPreferences(PREFS, MODE_PRIVATE).edit().putString("state", sb.toString()).putLong("ts", System.currentTimeMillis()).apply();
        return sb.toString();
    }

    void openBrowserSignIn() {
        try { startActivity(new Intent(Intent.ACTION_VIEW, Uri.parse(HOME + "app-signin?state=" + newState()))); } catch (Exception e) {}
    }

    void handleAuthIntent(Intent i) {
        if (i == null || i.getData() == null) return;
        Uri u = i.getData();
        if (!"yallaespanol".equals(u.getScheme()) || !"auth".equals(u.getHost())) return;
        String code = u.getQueryParameter("code");
        if (code == null || !code.matches("[a-f0-9]{64}")) return;
        pendingCode = code;
        runExchange();
    }

    void runExchange() {
        if (pendingCode == null || web == null) return;
        String url = web.getUrl();
        if (url == null || !url.startsWith(HOME)) { web.loadUrl(HOME); return; }
        android.content.SharedPreferences sp = getSharedPreferences(PREFS, MODE_PRIVATE);
        String st = sp.getString("state", null);
        long ts = sp.getLong("ts", 0);
        String code = pendingCode;
        pendingCode = null;
        sp.edit().clear().apply();
        if (st == null || System.currentTimeMillis() - ts > 600000 || !st.matches("[a-f0-9]{32}")) return;
        web.evaluateJavascript("fetch('api/appauth-exchange',{method:'POST',credentials:'same-origin',headers:{'Content-Type':'application/json','X-Yalla-App-Handoff':'1'},body:JSON.stringify({code:'" + code + "',state:'" + st + "'})}).then(function(){location.replace('/')}).catch(function(){})", null);
    }
    static final int REQ_MIC = 77;
    static final String HIDE_GOOGLE =
        "(function(){if(window.__yHide)return;window.__yHide=1;"
        + "function f(){var b=document.getElementById('google-button153');"
        + "if(b&&!b.__y){b.__y=1;b.style.cssText='display:block;padding:8px 0;text-align:center';"
        + "var del=!!document.getElementById('google-delete-confirm153');"
        + "if(del){b.textContent='\\u062d\\u0630\\u0641 \\u0627\\u0644\\u062d\\u0633\\u0627\\u0628 \\u0628\\u062c\\u0648\\u062c\\u0644 \\u0645\\u062a\\u0627\\u062d \\u0645\\u0646 \\u0627\\u0644\\u0645\\u062a\\u0635\\u0641\\u062d \\u0641\\u0642\\u0637.';}"
        + "else{var a=document.createElement('a');a.href='https://yalla-espanol.pages.dev/app-signin';a.className='btn';a.style.cssText='display:inline-block;text-decoration:none';"
        + "a.textContent='\\u0627\\u0644\\u062f\\u062e\\u0648\\u0644 \\u0628\\u062d\\u0633\\u0627\\u0628 Google';b.replaceChildren(a);}"
        + "new MutationObserver(function(){Array.prototype.forEach.call(b.children,function(c){if(c.tagName!=='A'&&!del)c.style.display='none';if(del)c.style.display='none'})}).observe(b,{childList:true});}}"
        + "f();new MutationObserver(f).observe(document.documentElement,{childList:true,subtree:true});})();";

    boolean online() {
        try {
            ConnectivityManager cm = (ConnectivityManager) getSystemService(CONNECTIVITY_SERVICE);
            Network n = cm.getActiveNetwork();
            if (n == null) return false;
            NetworkCapabilities c = cm.getNetworkCapabilities(n);
            return c != null && c.hasCapability(NetworkCapabilities.NET_CAPABILITY_INTERNET);
        } catch (Exception e) { return true; }
    }

    String mime(String path) {
        String ext = MimeTypeMap.getFileExtensionFromUrl(path);
        if ("js".equals(ext) || "mjs".equals(ext)) return "application/javascript";
        if ("json".equals(ext) || "webmanifest".equals(ext)) return "application/json";
        if ("svg".equals(ext)) return "image/svg+xml";
        if ("woff2".equals(ext)) return "font/woff2";
        if ("css".equals(ext)) return "text/css";
        if ("html".equals(ext)) return "text/html";
        String m = MimeTypeMap.getSingleton().getMimeTypeFromExtension(ext);
        return m == null ? "application/octet-stream" : m;
    }

    /* Offline fallback: serve the bundled copy of app code only when the device has no network. */
    WebResourceResponse bundled(Uri u) {
        if (!HOST.equals(u.getHost())) return null;
        String p = u.getPath();
        if (p == null || p.equals("") || p.equals("/")) p = "/index.html";
        if (p.contains("..")) return null;
        try {
            InputStream in = getAssets().open("www" + p);
            Map<String, String> h = new HashMap<>();
            h.put("Access-Control-Allow-Origin", "*");
            WebResourceResponse r = new WebResourceResponse(mime(p), "utf-8", in);
            r.setResponseHeaders(h);
            return r;
        } catch (Exception e) {
            return null;
        }
    }

    @Override
    protected void onCreate(Bundle b) {
        super.onCreate(b);
        FrameLayout root = new FrameLayout(this);
        root.setFitsSystemWindows(true);
        web = new WebView(this);
        root.addView(web, new FrameLayout.LayoutParams(ViewGroup.LayoutParams.MATCH_PARENT, ViewGroup.LayoutParams.MATCH_PARENT));
        setContentView(root);
        WebSettings s = web.getSettings();
        s.setJavaScriptEnabled(true);
        s.setDomStorageEnabled(true);
        s.setDatabaseEnabled(true);
        s.setMediaPlaybackRequiresUserGesture(false);
        s.setAllowFileAccess(false);
        s.setCacheMode(WebSettings.LOAD_DEFAULT);
        s.setUseWideViewPort(true);
        s.setLoadWithOverviewMode(false);
        s.setTextZoom(100);
        CookieManager.getInstance().setAcceptCookie(true);
        CookieManager.getInstance().setAcceptThirdPartyCookies(web, true);
        if (Build.VERSION.SDK_INT >= 24) {
            ServiceWorkerController.getInstance().setServiceWorkerClient(new ServiceWorkerClient() {
                @Override public WebResourceResponse shouldInterceptRequest(WebResourceRequest r) {
                    if (!online() && "GET".equals(r.getMethod())) return bundled(r.getUrl());
                    return null;
                }
            });
        }
        web.setWebChromeClient(new WebChromeClient() {
            @Override public void onPermissionRequest(final PermissionRequest req) {
                boolean mic = false;
                for (String r : req.getResources()) if (PermissionRequest.RESOURCE_AUDIO_CAPTURE.equals(r)) mic = true;
                if (!mic) { req.deny(); return; }
                if (checkSelfPermission(Manifest.permission.RECORD_AUDIO) == PackageManager.PERMISSION_GRANTED) {
                    req.grant(new String[]{PermissionRequest.RESOURCE_AUDIO_CAPTURE});
                } else {
                    pending = req;
                    requestPermissions(new String[]{Manifest.permission.RECORD_AUDIO}, REQ_MIC);
                }
            }
        });
        web.setWebViewClient(new WebViewClient() {
            @Override public void onPageFinished(WebView v, String url) {
                v.evaluateJavascript(HIDE_GOOGLE, null);
                runExchange();
            }
            @Override public boolean onRenderProcessGone(WebView v, RenderProcessGoneDetail d) {
                recreate();
                return true;
            }
            @Override public WebResourceResponse shouldInterceptRequest(WebView v, WebResourceRequest r) {
                if (!online() && "GET".equals(r.getMethod())) return bundled(r.getUrl());
                return null;
            }
            @Override public boolean shouldOverrideUrlLoading(WebView v, WebResourceRequest r) {
                Uri u = r.getUrl();
                if (HOST.equals(u.getHost()) && ("/app-signin".equals(u.getPath()) || "/app-signin.html".equals(u.getPath()))) { openBrowserSignIn(); return true; }
                if (HOST.equals(u.getHost())) return false;
                String sc = u.getScheme();
                if ("http".equals(sc) || "https".equals(sc) || "mailto".equals(sc) || "tel".equals(sc)) {
                    try { startActivity(new Intent(Intent.ACTION_VIEW, u)); } catch (Exception e) {}
                    return true;
                }
                return false;
            }
        });
        if (b != null) web.restoreState(b); else web.loadUrl(HOME);
        handleAuthIntent(getIntent());
    }

    @Override protected void onNewIntent(Intent i) { super.onNewIntent(i); setIntent(i); handleAuthIntent(i); }

    @Override public void onRequestPermissionsResult(int code, String[] perms, int[] res) {
        if (code == REQ_MIC && pending != null) {
            if (res.length > 0 && res[0] == PackageManager.PERMISSION_GRANTED)
                pending.grant(new String[]{PermissionRequest.RESOURCE_AUDIO_CAPTURE});
            else pending.deny();
            pending = null;
        }
    }

    @Override protected void onSaveInstanceState(Bundle o) { super.onSaveInstanceState(o); web.saveState(o); }

    @Override public void onBackPressed() {
        if (web.canGoBack()) web.goBack(); else finish();
    }

    @Override protected void onPause() { super.onPause(); CookieManager.getInstance().flush(); web.onPause(); }
    @Override protected void onResume() { super.onResume(); web.onResume(); }
}
