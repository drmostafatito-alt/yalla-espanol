# Yalla Español (يلا إسباني)

Spanish course for Arabic speakers. Static web app plus Cloudflare Pages Functions backend.

- `public/`: static site, current release 401 (app bundle, lexicon, direct and reverse dictionary bundles, fonts, images).
- `functions/`: Pages Functions (accounts, sync, curriculum payloads).
- `wrangler.jsonc`, `prepare.mjs`: Cloudflare Pages config and the step that copies an approved release into `public/`.

Not included: hosted audio (`audio/`, `audio-sprites/`, about 1.2 GB, served from the live site), older release bundles, and all secrets. API tokens, email keys and OAuth secrets are configured in Cloudflare, never in this repo.

Live site: https://yalla-espanol.pages.dev/
