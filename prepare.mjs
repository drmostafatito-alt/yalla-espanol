import {cp,writeFile} from 'node:fs/promises';
const source=process.argv[2];if(!source)throw Error('Pass the exact approved release public directory.');
await cp(source,new URL('./public/',import.meta.url),{recursive:true});
await writeFile(new URL('./public/_routes.json',import.meta.url),JSON.stringify({version:1,include:['/api/*'],exclude:[]}));
console.log('Prepared static assets and API-only Function routes. No deployment performed.');
