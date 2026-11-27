set -e
export JAVA_HOME=$(ls -d /downloads/android/jdk-17*); export PATH=$JAVA_HOME/bin:$PATH; SDK=/downloads/android/sdk; BT=$SDK/build-tools/34.0.0; AJ=$SDK/platforms/android-34/android.jar
cd /downloads/android/app; rm -rf build; mkdir -p build/cls
$BT/aapt2 compile --dir res -o build/res.zip
$BT/aapt2 link -o build/base.apk -I $AJ --manifest AndroidManifest.xml -A assets --min-sdk-version 24 --target-sdk-version 34 build/res.zip
javac -source 8 -target 8 -cp $AJ -d build/cls src/com/yalla/espanol/MainActivity.java 2>&1 | grep -i error || true
$BT/d8 --min-api 24 --lib $AJ --output build $(find build/cls -name '*.class')
cp build/base.apk build/u.apk; (cd build && zip -q -j u.apk classes.dex)
$BT/zipalign -f -p 4 build/u.apk build/a.apk
$BT/apksigner sign --ks ../debug.keystore --ks-pass pass:android --key-pass pass:android --ks-key-alias yalla --out ../YallaEspanol.apk build/a.apk
$BT/apksigner verify ../YallaEspanol.apk && ls -la ../YallaEspanol.apk
