'use strict';
const MANIFEST = 'flutter-app-manifest';
const TEMP = 'flutter-temp-cache';
const CACHE_NAME = 'flutter-app-cache';

const RESOURCES = {"flutter.js": "24bc71911b75b5f8135c949e27a2984e",
"icons/Icon-512.png": "96e752610906ba2a93c65f8abe1645f1",
"icons/Icon-maskable-512.png": "301a7604d45b3e739efc881eb04896ea",
"icons/Icon-192.png": "ac9a721a12bbc803b44f645561ecb1e1",
"icons/Icon-maskable-192.png": "c457ef57daa1d16f64b27b786ec2ea3c",
"manifest.json": "c648d529753d57cf1bb8229adaed4944",
"index.html": "a63e6f56128432467e3277a1e3007a71",
"/": "a63e6f56128432467e3277a1e3007a71",
"assets/shaders/stretch_effect.frag": "40d68efbbf360632f614c731219e95f0",
"assets/shaders/ink_sparkle.frag": "ecc85a2e95f5e9f53123dcaf8cb9b6ce",
"assets/AssetManifest.bin.json": "a87f36848da064c68212d3e809ea3bac",
"assets/assets/images/037_aborto.png": "cbe7d23eb4e569aec148e96a20669078",
"assets/assets/images/095_acerbo.png": "5fef800d23a4b8e2651224a7ae62c993",
"assets/assets/images/082_accontentare.png": "7c2ac670ef49788c4701c7ca7108d0cb",
"assets/assets/images/025_abile.png": "2986e9f79fd38bc51467e3d1aabc0c27",
"assets/assets/images/086_accorgersi.png": "d03f080b9844d9a97c0aaba87682d2a7",
"assets/assets/images/084_accordare.png": "65e40bb73b3459fd6b9d159f638be37c",
"assets/assets/images/026_abilita.png": "14270948c0b716e96bc93b5c093ef3da",
"assets/assets/images/062_accertamento.png": "fbd8d2725aea817773fb271847a1108a",
"assets/assets/images/090_accumulare.png": "7d2c73ae67ed07bdf8bbe96bbe4dd0a3",
"assets/assets/images/002_a_roma.png": "0017a8034c17e0ca71578571c59676de",
"assets/assets/images/021_abbraccio.png": "3b95f6062390a3f7f0d486185dcfaf32",
"assets/assets/images/012_abbeverare.png": "b65d54e1184bab189dca008d8b3b3a2b",
"assets/assets/images/060_accentare.png": "b203b053eb71478e0bfccc700a24ab4a",
"assets/assets/images/042_accademia.png": "b3fda0ca0b6ee5feb91793cd1dc51ad2",
"assets/assets/images/045_accampamento.png": "d2b319fc9f8a5869acabc773a43fed6b",
"assets/assets/images/071_acciacco.png": "1c96e0597d9ebd1342a5064735131271",
"assets/assets/images/100_acquario.png": "3933f52d5c3104a8487c7ef01391ad27",
"assets/assets/images/008_abbassare.png": "c4e2a9ffb4e6304135992a3780400905",
"assets/assets/images/001_a_alphabet.png": "3082d0af307dff3b0e267c265d8205f3",
"assets/assets/images/038_abruzzese.png": "8e64625946a272adcfbd1ecc321840ca",
"assets/assets/images/023_abbronzare.png": "92f9c29c4dac9a5f2b1a6c184a29f71d",
"assets/assets/images/081_acconsentire.png": "fdf610b8b9b59b712adb2f298f00c110",
"assets/assets/images/065_accesso.png": "ac136b34412fc807af4d01a09de3b9ca",
"assets/assets/images/019_abbottonare.png": "fc6ea264ef20e43308478a2b19634415",
"assets/assets/images/051_accecare.png": "e1169cb6f6788f3de54c7215178b21cd",
"assets/assets/images/056_accendere.png": "42eae89981cfeea578c27be7443fa10c",
"assets/assets/images/093_accusa.png": "6164183668cc08de50602b1ebaa99ac5",
"assets/assets/images/004_abbaiare.png": "61b439be6db889f3407eed13f9569c1c",
"assets/assets/images/099_acquarello.png": "b0abb3fd068d3a3dda0837e2adf18ead",
"assets/assets/images/040_abuso.png": "486eef55497b2c1bbe117c5fea000c37",
"assets/assets/images/006_abbandonato.png": "e6b7264fd35b0f1f847053bd6a32c8d0",
"assets/assets/images/043_accademico.png": "cccef6bc5748b8a72c7c0ef7ea069045",
"assets/assets/images/027_abisso.png": "aa5a0bba72445ca6b8045d56b8cf7728",
"assets/assets/images/049_accattone.png": "a2c3d2b582ada54ce4131668a13f6c7c",
"assets/assets/images/046_accanto.png": "12796c8cd591e3463ba92a7872f795a8",
"assets/assets/images/044_accadere.png": "b914bc5124fb7091b42d46d9d69fceee",
"assets/assets/images/055_accelerazione.png": "6a0e8e60c03a6e31db642222c45a3781",
"assets/assets/images/031_abito.png": "838d63f3f79840fec8bd04ec5a81ec79",
"assets/assets/images/087_accorrere.png": "610eb7d808c48179cbf1fb8fb4ef1a5a",
"assets/assets/images/015_abbonamento.png": "76db1e870f1770514f6b73153a985bee",
"assets/assets/images/013_abbigliamento.png": "f2e8010147cd56a22820997d31da8d42",
"assets/assets/images/035_abolire.png": "65ccb7121719f8ff15d19f7d636e3dcd",
"assets/assets/images/088_accostare.png": "a5dffd3cd5c0d371b6f52f2ccffbe022",
"assets/assets/images/089_accudire.png": "deedc15f85916dd748d84e609d2ac90a",
"assets/assets/images/069_accettare.png": "58c7de2396bd618e63e1fbae08d314cb",
"assets/assets/images/074_acciuga.png": "c2033a0a00f4a6d0854471b60e0734e9",
"assets/assets/images/032_abituale.png": "a62ed9173d150cfbe5f24fcad65cc9ae",
"assets/assets/images/077_accogliere.png": "e7c05c2a9c08e676522b3220a8099ac3",
"assets/assets/images/005_abbandonare.png": "38bdb8659e798be1f2e386f3796614f8",
"assets/assets/images/076_accoglienza.png": "9ce705174b8c67efabbe2b2acb97a4d5",
"assets/assets/images/070_acchiappare.png": "dfdfc7c7135313c490ac9985d12ae56d",
"assets/assets/images/075_accogliente.png": "7810ee0d91465b0936b7dbae8de7d918",
"assets/assets/images/080_accompagnare.png": "3722382fc899dd2f5617d4bb9e0bbae1",
"assets/assets/images/067_accetta.png": "cce56bd24eedb20d43c735cc9739135c",
"assets/assets/images/017_abbondante.png": "9e73e28c7d93967a3de26763759e7b6e",
"assets/assets/images/047_accappatoio.png": "63b6f0371c3f860755dcb1e3773f53cb",
"assets/assets/images/085_accordo.png": "34a55293d7471355f48b74ec2ec3d19f",
"assets/assets/images/041_acca.png": "76d0c44e056282a663f870892f252167",
"assets/assets/images/059_accenno.png": "4a4346b8a9d0da0923a8cd5cc45f4a7d",
"assets/assets/images/033_abituare.png": "02fa33b2ef68e57145ad53a4f93f267b",
"assets/assets/images/007_abbandono.png": "f02f1aaf174295f8b9006639b002309f",
"assets/assets/images/003_abbagliante.png": "e75a34dd81290fc5dffb33adc8d5c237",
"assets/assets/images/010_abbastanza.png": "8807673f926104607eb281152b65541c",
"assets/assets/images/073_accidente.png": "f5f87d558d81557c714cac6ab6c86934",
"assets/assets/images/014_abbinare.png": "c71358f70b73f3bad4e6f4fc5d0d2104",
"assets/assets/images/018_abbondare.png": "f64203291a58177750915179db74137c",
"assets/assets/images/092_accurato.png": "8601b325ffbf64ee5a04c5fe4354287b",
"assets/assets/images/057_accendino.png": "2b4753faddb06b648eec5887b37459da",
"assets/assets/images/097_acido.png": "211e0fed5a228c84b46cb371d593c81e",
"assets/assets/images/036_abortire.png": "347832f263e2c550cbcfbd07162114a3",
"assets/assets/images/072_acciaio.png": "3874ef2efc1d9aac3e0533eb46a3434e",
"assets/assets/images/016_abbonare.png": "82bbe1be32ef92bf9c660135768785ce",
"assets/assets/images/078_accoltellare.png": "4e5b57b1e86e443e577770465aa2aeb8",
"assets/assets/images/030_abitazione.png": "db61092650e61ee739612b1f2a5b0989",
"assets/assets/images/063_accertare.png": "258837ca99de18859d943071359ab9db",
"assets/assets/images/083_accorciare.png": "33b5ada39ecd6cba0d3525787054f658",
"assets/assets/images/054_acceleratore.png": "a4b36ccb835217253fa96ad8b276c2a1",
"assets/assets/images/039_abusare.png": "554010c80908cff89b82218a5168fc00",
"assets/assets/images/022_abbreviare.png": "ca68a62768b94c7496e5a0ecf9789acf",
"assets/assets/images/066_accessorio.png": "12d0a62b1b44b276c062634b5a85b465",
"assets/assets/images/034_abitudine.png": "62c040914e6520b8ecb4f5005aba2037",
"assets/assets/images/048_accarezzare.png": "44a3a9d25a00e29c6250a4569db1ef2e",
"assets/assets/images/050_accavallare.png": "f08d516a943e12eeeaba7d4db5c990dc",
"assets/assets/images/096_aceto.png": "a18ee2aef99ed702c659ebf56f395c96",
"assets/assets/images/029_abitare.png": "377fb7080ecbcdce11b981dd97ef8a76",
"assets/assets/images/079_accomodare.png": "1d1e1ae13e5c464c552e7639d14ea0d9",
"assets/assets/images/061_accento.png": "9b44a6ba05f9f77f49bd37db08d68f9a",
"assets/assets/images/091_accumulatore.png": "0719a0d7b268cf1700efaa63bdbfec07",
"assets/assets/images/053_accelerare.png": "76c7868a58dbe8bba676c8efffbe0a8f",
"assets/assets/images/094_accusare.png": "55185e546ffdceaf54772b6d72129e31",
"assets/assets/images/020_abbracciare.png": "c93546f0403261e39b8baabe3e8dd7e4",
"assets/assets/images/068_accettabile.png": "54265991299e3f7840b4aa1fd4e9b87b",
"assets/assets/images/058_accennare.png": "ef25407085be33bf9b101eba07ccef66",
"assets/assets/images/098_acqua.png": "12c29fd67b41f526b687c96e0cf4a926",
"assets/assets/images/028_abitante.png": "f3f0393f05f46216b0355e066257fe67",
"assets/assets/images/064_acceso.png": "7d3dc1fd3a6b7a4abca36e9f4f37f774",
"assets/assets/images/009_abbasso.png": "b71f7ea0184bec60ac8159bc9faea40f",
"assets/assets/images/024_abete.png": "c83a9ecd1122d837a84f61f1db2ce29e",
"assets/assets/images/052_accedere.png": "3aae161318b414f3823eeecbcf12b289",
"assets/assets/images/011_abbattere.png": "b7986967164c0777fe1c9435e49d4683",
"assets/assets/data/vocab_part1.json": "6e61f546752020407ac6611f1edea792",
"assets/assets/data/vocab.json": "5d4fd7ccbfacd0b7d2a11f96ad028c28",
"assets/fonts/MaterialIcons-Regular.otf": "2bdc07d1267ce30e48b52858c06b3304",
"assets/NOTICES": "44ad8f6559af3cef17e6f9f3da53f4c4",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "33b7d9392238c04c131b6ce224e13711",
"assets/FontManifest.json": "dc3d03800ccca4601324923c0b1d6d57",
"assets/AssetManifest.bin": "d94d2997fa390fcb23da6483121f7ee1",
"canvaskit/chromium/canvaskit.wasm": "a726e3f75a84fcdf495a15817c63a35d",
"canvaskit/chromium/canvaskit.js": "a80c765aaa8af8645c9fb1aae53f9abf",
"canvaskit/chromium/canvaskit.js.symbols": "e2d09f0e434bc118bf67dae526737d07",
"canvaskit/skwasm_heavy.wasm": "b0be7910760d205ea4e011458df6ee01",
"canvaskit/skwasm_heavy.js.symbols": "0755b4fb399918388d71b59ad390b055",
"canvaskit/skwasm.js": "8060d46e9a4901ca9991edd3a26be4f0",
"canvaskit/canvaskit.wasm": "9b6a7830bf26959b200594729d73538e",
"canvaskit/skwasm_heavy.js": "740d43a6b8240ef9e23eed8c48840da4",
"canvaskit/canvaskit.js": "8331fe38e66b3a898c4f37648aaf7ee2",
"canvaskit/skwasm.wasm": "7e5f3afdd3b0747a1fd4517cea239898",
"canvaskit/canvaskit.js.symbols": "a3c9f77715b642d0437d9c275caba91e",
"canvaskit/skwasm.js.symbols": "3a4aadf4e8141f284bd524976b1d6bdc",
"favicon.png": "5dcef449791fa27946b3d35ad8803796",
"flutter_bootstrap.js": "8bd2dca4fb0a6bb863369e364418912c",
"version.json": "612599dc5bea04eeecf03af277de9630",
"main.dart.js": "508b3b52f2544b425a24c7f0e42cefb1"};
// The application shell files that are downloaded before a service worker can
// start.
const CORE = ["main.dart.js",
"index.html",
"flutter_bootstrap.js",
"assets/AssetManifest.bin.json",
"assets/FontManifest.json"];

// During install, the TEMP cache is populated with the application shell files.
self.addEventListener("install", (event) => {
  self.skipWaiting();
  return event.waitUntil(
    caches.open(TEMP).then((cache) => {
      return cache.addAll(
        CORE.map((value) => new Request(value, {'cache': 'reload'})));
    })
  );
});
// During activate, the cache is populated with the temp files downloaded in
// install. If this service worker is upgrading from one with a saved
// MANIFEST, then use this to retain unchanged resource files.
self.addEventListener("activate", function(event) {
  return event.waitUntil(async function() {
    try {
      var contentCache = await caches.open(CACHE_NAME);
      var tempCache = await caches.open(TEMP);
      var manifestCache = await caches.open(MANIFEST);
      var manifest = await manifestCache.match('manifest');
      // When there is no prior manifest, clear the entire cache.
      if (!manifest) {
        await caches.delete(CACHE_NAME);
        contentCache = await caches.open(CACHE_NAME);
        for (var request of await tempCache.keys()) {
          var response = await tempCache.match(request);
          await contentCache.put(request, response);
        }
        await caches.delete(TEMP);
        // Save the manifest to make future upgrades efficient.
        await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
        // Claim client to enable caching on first launch
        self.clients.claim();
        return;
      }
      var oldManifest = await manifest.json();
      var origin = self.location.origin;
      for (var request of await contentCache.keys()) {
        var key = request.url.substring(origin.length + 1);
        if (key == "") {
          key = "/";
        }
        // If a resource from the old manifest is not in the new cache, or if
        // the MD5 sum has changed, delete it. Otherwise the resource is left
        // in the cache and can be reused by the new service worker.
        if (!RESOURCES[key] || RESOURCES[key] != oldManifest[key]) {
          await contentCache.delete(request);
        }
      }
      // Populate the cache with the app shell TEMP files, potentially overwriting
      // cache files preserved above.
      for (var request of await tempCache.keys()) {
        var response = await tempCache.match(request);
        await contentCache.put(request, response);
      }
      await caches.delete(TEMP);
      // Save the manifest to make future upgrades efficient.
      await manifestCache.put('manifest', new Response(JSON.stringify(RESOURCES)));
      // Claim client to enable caching on first launch
      self.clients.claim();
      return;
    } catch (err) {
      // On an unhandled exception the state of the cache cannot be guaranteed.
      console.error('Failed to upgrade service worker: ' + err);
      await caches.delete(CACHE_NAME);
      await caches.delete(TEMP);
      await caches.delete(MANIFEST);
    }
  }());
});
// The fetch handler redirects requests for RESOURCE files to the service
// worker cache.
self.addEventListener("fetch", (event) => {
  if (event.request.method !== 'GET') {
    return;
  }
  var origin = self.location.origin;
  var key = event.request.url.substring(origin.length + 1);
  // Redirect URLs to the index.html
  if (key.indexOf('?v=') != -1) {
    key = key.split('?v=')[0];
  }
  if (event.request.url == origin || event.request.url.startsWith(origin + '/#') || key == '') {
    key = '/';
  }
  // If the URL is not the RESOURCE list then return to signal that the
  // browser should take over.
  if (!RESOURCES[key]) {
    return;
  }
  // If the URL is the index.html, perform an online-first request.
  if (key == '/') {
    return onlineFirst(event);
  }
  event.respondWith(caches.open(CACHE_NAME)
    .then((cache) =>  {
      return cache.match(event.request).then((response) => {
        // Either respond with the cached resource, or perform a fetch and
        // lazily populate the cache only if the resource was successfully fetched.
        return response || fetch(event.request).then((response) => {
          if (response && Boolean(response.ok)) {
            cache.put(event.request, response.clone());
          }
          return response;
        });
      })
    })
  );
});
self.addEventListener('message', (event) => {
  // SkipWaiting can be used to immediately activate a waiting service worker.
  // This will also require a page refresh triggered by the main worker.
  if (event.data === 'skipWaiting') {
    self.skipWaiting();
    return;
  }
  if (event.data === 'downloadOffline') {
    downloadOffline();
    return;
  }
});
// Download offline will check the RESOURCES for all files not in the cache
// and populate them.
async function downloadOffline() {
  var resources = [];
  var contentCache = await caches.open(CACHE_NAME);
  var currentContent = {};
  for (var request of await contentCache.keys()) {
    var key = request.url.substring(origin.length + 1);
    if (key == "") {
      key = "/";
    }
    currentContent[key] = true;
  }
  for (var resourceKey of Object.keys(RESOURCES)) {
    if (!currentContent[resourceKey]) {
      resources.push(resourceKey);
    }
  }
  return contentCache.addAll(resources);
}
// Attempt to download the resource online before falling back to
// the offline cache.
function onlineFirst(event) {
  return event.respondWith(
    fetch(event.request).then((response) => {
      return caches.open(CACHE_NAME).then((cache) => {
        cache.put(event.request, response.clone());
        return response;
      });
    }).catch((error) => {
      return caches.open(CACHE_NAME).then((cache) => {
        return cache.match(event.request).then((response) => {
          if (response != null) {
            return response;
          }
          throw error;
        });
      });
    })
  );
}
