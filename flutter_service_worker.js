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
"assets/AssetManifest.bin.json": "0c1fff59427656190b0390a19c0f6ff8",
"assets/assets/images/208_aguzzo.png": "5186071ed1d86b493bec3dd603e9cbc4",
"assets/assets/images/037_aborto.png": "cbe7d23eb4e569aec148e96a20669078",
"assets/assets/images/313_ammuffire.png": "03a1514a507292ff5e239713e97851a8",
"assets/assets/images/351_annodare.png": "ec52b356003302041349adaa175a412f",
"assets/assets/images/095_acerbo.png": "5fef800d23a4b8e2651224a7ae62c993",
"assets/assets/images/082_accontentare.png": "7c2ac670ef49788c4701c7ca7108d0cb",
"assets/assets/images/025_abile.png": "2986e9f79fd38bc51467e3d1aabc0c27",
"assets/assets/images/086_accorgersi.png": "d03f080b9844d9a97c0aaba87682d2a7",
"assets/assets/images/270_altezza.png": "ec4124afa71e7b6e4b0c3db03873d840",
"assets/assets/images/110_acrobazia.png": "fe5a5766c1b4e2d231a2196d96aad2f4",
"assets/assets/images/344_animato.png": "dee84c720afab7feb156ae47ad39945a",
"assets/assets/images/084_accordare.png": "65e40bb73b3459fd6b9d159f638be37c",
"assets/assets/images/176_adulazione.png": "af6515516e79408152e8df61d2f56e41",
"assets/assets/images/026_abilita.png": "14270948c0b716e96bc93b5c093ef3da",
"assets/assets/images/241_alleggerire.png": "d55ed3ccaaee159414edc6b4a4999d08",
"assets/assets/images/062_accertamento.png": "fbd8d2725aea817773fb271847a1108a",
"assets/assets/images/293_americano.png": "99641e41351ba0917f4e8ce99de9c959",
"assets/assets/images/238_allearsi.png": "ac38bcfa54805f77d1a630d7594b615e",
"assets/assets/images/103_acquazzone.png": "70adf38766f01390f2e81da6d652e772",
"assets/assets/images/196_affacciarsi.png": "f31fb8b55e3996dfde54467539e3df29",
"assets/assets/images/189_aeroplano.png": "13426adb7044d2c45b73e335d80a3a47",
"assets/assets/images/129_addirsi.png": "5ff73bf34e36ee06fbbd18805d67a3f8",
"assets/assets/images/117_adattabile.png": "0e15ba4b39c80deddb4f499aa7fd6ab6",
"assets/assets/images/107_acquistare.png": "882dca2b12ad9e111d52d7e11fad77a4",
"assets/assets/images/302_ammazzare.png": "594d0067176ac5713e4381be56a8447b",
"assets/assets/images/181_adunanza.png": "af4e02e1070a631ea17db7e43966be0c",
"assets/assets/images/227_alimentari.png": "a6dfdd3ba066a9bd575e6283b58600fa",
"assets/assets/images/146_adempiere.png": "bce23312f9234d1b9ee7cbdfcdbfcdf3",
"assets/assets/images/141_addurre.png": "80d0a778e7c31080fdc76bfcfc3c6ec7",
"assets/assets/images/349_anniversario.png": "b0f5bd6270e08152d362dc05cbd1ff7b",
"assets/assets/images/160_adirarsi.png": "6db23e8fb718f21a235d9be1a4f536f1",
"assets/assets/images/106_acquirente.png": "51f0a9425fbf2dcefb1463d824381bc7",
"assets/assets/images/090_accumulare.png": "7d2c73ae67ed07bdf8bbe96bbe4dd0a3",
"assets/assets/images/155_adesso.png": "81950a22af3e4806499d5ddf56ab91ca",
"assets/assets/images/184_adunco.png": "828c2dae0f19cb6ac2c4f7603046e8d8",
"assets/assets/images/002_a_roma.png": "0017a8034c17e0ca71578571c59676de",
"assets/assets/images/209_aiuola.png": "b4741c0e80f9a3aa52c76f1ff8805209",
"assets/assets/images/264_altare.png": "2cbe248793357d1609f47baa5da858c8",
"assets/assets/images/021_abbraccio.png": "3b95f6062390a3f7f0d486185dcfaf32",
"assets/assets/images/130_addirittura.png": "e883a032c58ded137f762729c52b6fe1",
"assets/assets/images/012_abbeverare.png": "b65d54e1184bab189dca008d8b3b3a2b",
"assets/assets/images/060_accentare.png": "b203b053eb71478e0bfccc700a24ab4a",
"assets/assets/images/121_addebitare.png": "fcfd2665137494b9443965522561ba44",
"assets/assets/images/322_analitico.png": "330c4c2609feedae5d32993e45405dee",
"assets/assets/images/143_adeguare.png": "934412e674e7c9b74dac86c534ea7798",
"assets/assets/images/042_accademia.png": "b3fda0ca0b6ee5feb91793cd1dc51ad2",
"assets/assets/images/045_accampamento.png": "d2b319fc9f8a5869acabc773a43fed6b",
"assets/assets/images/071_acciacco.png": "1c96e0597d9ebd1342a5064735131271",
"assets/assets/images/100_acquario.png": "3933f52d5c3104a8487c7ef01391ad27",
"assets/assets/images/342_animale_agg.png": "468f42ec947057072a4afcba8287471b",
"assets/assets/images/253_allontanare.png": "fc5d07bf296682ad20ea25ff1f9d0637",
"assets/assets/images/008_abbassare.png": "c4e2a9ffb4e6304135992a3780400905",
"assets/assets/images/248_allergia.png": "eb3f2f1077d5c4ead2e0240d84c1ed6b",
"assets/assets/images/353_annotare.png": "221bbbf4386fd86b412094f686e492bb",
"assets/assets/images/297_ammalarsi.png": "ff81ed1ebbf0e700697a68bf9178f0eb",
"assets/assets/images/001_a_alphabet.png": "3082d0af307dff3b0e267c265d8205f3",
"assets/assets/images/214_albanese.png": "1f2bd5eebea3b3fca83ae6de8c5b9aba",
"assets/assets/images/308_ammissione.png": "ef9067558435321efb1c672d08ad67a8",
"assets/assets/images/312_ammucchiare.png": "026dbf1ea8a2979da77bfe514459af65",
"assets/assets/images/296_ammaccare.png": "c7dee3fa08935d7488b51d732fce1869",
"assets/assets/images/287_ambientale.png": "3681d06d736bc1f4ca83b01e8ae529db",
"assets/assets/images/233_allargare.png": "37b8b2993976d52b917b7cc65290e27c",
"assets/assets/images/038_abruzzese.png": "8e64625946a272adcfbd1ecc321840ca",
"assets/assets/images/289_ambiente.png": "e62f9df88e309b0275aaa0c7e4f52921",
"assets/assets/images/167_adorare.png": "398df185978deaafc2e5f0d727b3ea8c",
"assets/assets/images/023_abbronzare.png": "92f9c29c4dac9a5f2b1a6c184a29f71d",
"assets/assets/images/122_addebito.png": "ad9bf9cfba8b18bca1e62dc95a11a42c",
"assets/assets/images/232_allagare.png": "c8a61527aa7a1c0c091d6a5b9cea35dd",
"assets/assets/images/170_adorno.png": "b26510e8d256e736d81785cbf4b7cc56",
"assets/assets/images/203_affare.png": "f63605a960cecf647b2715b7921417ee",
"assets/assets/images/081_acconsentire.png": "fdf610b8b9b59b712adb2f298f00c110",
"assets/assets/images/065_accesso.png": "ac136b34412fc807af4d01a09de3b9ca",
"assets/assets/images/205_affascinante.png": "20f9ef7b01fbddc6d964eceb5875b785",
"assets/assets/images/185_aerare.png": "650f58b1d684fb4d71771a9a99cc915e",
"assets/assets/images/201_affanno.png": "e357351e288760f2e0b65ab23ac14eca",
"assets/assets/images/019_abbottonare.png": "fc6ea264ef20e43308478a2b19634415",
"assets/assets/images/265_alterare.png": "023313f4a9a20ba02551e77db84ec069",
"assets/assets/images/304_amministrativo.png": "c79cef0f4e554135ccd791c31ac7ff87",
"assets/assets/images/298_ammalato.png": "7af68c338ae43f7920ca8dcd51a44b42",
"assets/assets/images/051_accecare.png": "e1169cb6f6788f3de54c7215178b21cd",
"assets/assets/images/056_accendere.png": "42eae89981cfeea578c27be7443fa10c",
"assets/assets/images/119_adattare.png": "22fe32f99fc4add9489724757612e131",
"assets/assets/images/138_addormentarsi.png": "6825550e5875d64cba8e518cd924063a",
"assets/assets/images/198_affamato.png": "a1e8f9598330acf9765dc60d61dcd125",
"assets/assets/images/242_allegria.png": "e8c530c699031f7896ca56d3aa389e36",
"assets/assets/images/244_allenamento.png": "e06d0d0951f545b10db327be4d5ca956",
"assets/assets/images/093_accusa.png": "6164183668cc08de50602b1ebaa99ac5",
"assets/assets/images/276_altro.png": "28a3fbb3d4f4dcf89c9198d6e2a3b8e3",
"assets/assets/images/134_addolcire.png": "dd30714744e14887e5770120fc1faa5b",
"assets/assets/images/234_allarmare.png": "463f48db2e970900c72079b101f69cdc",
"assets/assets/images/266_alternare.png": "045e5078f985b777b5ad635bb8d5321b",
"assets/assets/images/339_angoscia.png": "c32f4169570bcb150c2e506023064c7a",
"assets/assets/images/315_amoroso.png": "9a1a80522ee55eebde4bf6675af3ba32",
"assets/assets/images/301_ammasso.png": "125862b284519ff7ebabf2c0b144d619",
"assets/assets/images/290_ambito.png": "2880c2564e7e81f1c17035c9e9551b90",
"assets/assets/images/331_ancorare.png": "5dfc80164c0df18071587ae5d996b7b8",
"assets/assets/images/152_adescare.png": "6424f522473b629b3c48fbcc9fea5a6d",
"assets/assets/images/271_alto.png": "0d863b218c948440994b5a6e3ef40d11",
"assets/assets/images/004_abbaiare.png": "61b439be6db889f3407eed13f9569c1c",
"assets/assets/images/168_adorazione.png": "bdac1ec2c0fc3f9c89c01b585ccd9371",
"assets/assets/images/193_affabile.png": "4c488339f3c5615ba3a275c42679f258",
"assets/assets/images/295_amico.png": "ae4b7c11b6d5154c214511592c219f0f",
"assets/assets/images/099_acquarello.png": "b0abb3fd068d3a3dda0837e2adf18ead",
"assets/assets/images/204_agricoltore.png": "62f3c897fe99aef33745aac8b12ae114",
"assets/assets/images/324_analogo.png": "cef8a79868644a584ba30cb109983914",
"assets/assets/images/040_abuso.png": "486eef55497b2c1bbe117c5fea000c37",
"assets/assets/images/127_addiaccio.png": "19af011ca5a932f4a97db9986b4ea860",
"assets/assets/images/211_aiuto.png": "456552cad34ed5e8d5e07b46c28c78b1",
"assets/assets/images/006_abbandonato.png": "e6b7264fd35b0f1f847053bd6a32c8d0",
"assets/assets/images/043_accademico.png": "cccef6bc5748b8a72c7c0ef7ea069045",
"assets/assets/images/314_amore.png": "b40f35bb0052c100683a25a36ad67829",
"assets/assets/images/124_addestramento.png": "8d7df330443a1a578678f899f8d4c556",
"assets/assets/images/229_alimento.png": "6cd95c059583e5278e9276167c1ffd79",
"assets/assets/images/027_abisso.png": "aa5a0bba72445ca6b8045d56b8cf7728",
"assets/assets/images/212_ala.png": "38ac0a38a31c90c1e260e14d2df9c270",
"assets/assets/images/049_accattone.png": "a2c3d2b582ada54ce4131668a13f6c7c",
"assets/assets/images/142_adeguamento.png": "42ba19a258816b700a4c272dde5e322a",
"assets/assets/images/299_ammanettare.png": "62c8e1d99240d85fb20e499eaa34880a",
"assets/assets/images/309_ammobiliare.png": "640dea80b0ec0c471775a6383adcfcf2",
"assets/assets/images/204_affarista.png": "e6c82ea5d5a1e4b9f18da636f7552719",
"assets/assets/images/046_accanto.png": "12796c8cd591e3463ba92a7872f795a8",
"assets/assets/images/044_accadere.png": "b914bc5124fb7091b42d46d9d69fceee",
"assets/assets/images/055_accelerazione.png": "6a0e8e60c03a6e31db642222c45a3781",
"assets/assets/images/031_abito.png": "838d63f3f79840fec8bd04ec5a81ec79",
"assets/assets/images/182_adunare.png": "19f6eeb9e5745d46335b1c5d65dc20de",
"assets/assets/images/205_agricoltura.png": "f3b7ed9c3a90ee2db2d3fc193984e25d",
"assets/assets/images/183_adunata.png": "966ad48369db67c3138c67abfab60b51",
"assets/assets/images/216_albero.png": "7fedf5f201715e0d209896e04fe64a31",
"assets/assets/images/319_analcolico.png": "448757ccef863e45472b3bd1710a6f95",
"assets/assets/images/210_aiutare.png": "8b1a2bcd02b4c5feb90afa7789c83e26",
"assets/assets/images/113_acutezza.png": "0f4ac4f9d61c1ada8dbdb225d0d3b6a4",
"assets/assets/images/300_ammassare.png": "8c5c5a20d62bcbe10efce299a57ad65c",
"assets/assets/images/087_accorrere.png": "610eb7d808c48179cbf1fb8fb4ef1a5a",
"assets/assets/images/015_abbonamento.png": "76db1e870f1770514f6b73153a985bee",
"assets/assets/images/286_ambasciata.png": "639691bd89c5e0b11c2d0ba8b98a1f83",
"assets/assets/images/258_allungare.png": "40ea1ecfe4513e9de0f536343b0e3c4b",
"assets/assets/images/013_abbigliamento.png": "f2e8010147cd56a22820997d31da8d42",
"assets/assets/images/191_aerosol.png": "fdbd24de0c6b1ab05fe89d00a0960b5b",
"assets/assets/images/169_adornare.png": "d566718d65278b2d71ac6375c402f3c6",
"assets/assets/images/035_abolire.png": "65ccb7121719f8ff15d19f7d636e3dcd",
"assets/assets/images/140_addosso.png": "9166fd6b4f35c37b5273579e1696c94e",
"assets/assets/images/088_accostare.png": "a5dffd3cd5c0d371b6f52f2ccffbe022",
"assets/assets/images/089_accudire.png": "deedc15f85916dd748d84e609d2ac90a",
"assets/assets/images/150_aderire.png": "4794ea58e66ecfe5ca53d6158d73c995",
"assets/assets/images/069_accettare.png": "58c7de2396bd618e63e1fbae08d314cb",
"assets/assets/images/153_adesione.png": "ac9342dbe4cee395ee8ac80579fa398d",
"assets/assets/images/074_acciuga.png": "c2033a0a00f4a6d0854471b60e0734e9",
"assets/assets/images/177_adulterare.png": "1f3539fb99c0cdcde4cca440a12a4f42",
"assets/assets/images/218_album.png": "94a6ec9d8a006e48c19508cdf0c07602",
"assets/assets/images/281_alzare.png": "4ddbab9c5a38f521dbf4cc0a2664bafe",
"assets/assets/images/032_abituale.png": "a62ed9173d150cfbe5f24fcad65cc9ae",
"assets/assets/images/077_accogliere.png": "e7c05c2a9c08e676522b3220a8099ac3",
"assets/assets/images/180_adulto.png": "b7cff4c3598c6b78c810869ba8cb93a1",
"assets/assets/images/221_alfabeto.png": "eafa66a6884c50586a2177cda65ae02e",
"assets/assets/images/136_addomesticare.png": "e7c91ff45f7c1a5ae6eaeb425cf20acc",
"assets/assets/images/187_aereo.png": "3188cceeb656cc6e5106805fa6ef87aa",
"assets/assets/images/005_abbandonare.png": "38bdb8659e798be1f2e386f3796614f8",
"assets/assets/images/145_adeguato.png": "4cb0becb917a45af2375c1c72b2c1d81",
"assets/assets/images/165_adoperare.png": "7a773bfc1ee37507377d34220f0e05c5",
"assets/assets/images/076_accoglienza.png": "9ce705174b8c67efabbe2b2acb97a4d5",
"assets/assets/images/162_adolescente.png": "bbbe47a1c59901ff5c8c08ace18559ae",
"assets/assets/images/215_albergo.png": "84bbbfe753d4be9cad71206e1cb77fa5",
"assets/assets/images/252_alloggio.png": "bbd62f93bdc32b3919534b74e2fbc9dd",
"assets/assets/images/306_amministrazione.png": "e897e0ab11a3343bb03df16b6ce26343",
"assets/assets/images/158_adipe.png": "cb5602a5d89e7d5f36914611753b302e",
"assets/assets/images/108_acquisto.png": "e8318bb0ed6918143f11008b4cddb1bf",
"assets/assets/images/282_amante.png": "1edb30f8eae7f97c0509da1466b0a1e0",
"assets/assets/images/070_acchiappare.png": "dfdfc7c7135313c490ac9985d12ae56d",
"assets/assets/images/105_acqueo.png": "87bb4514b9b00e378bbcafdc71f06488",
"assets/assets/images/220_alcuno.png": "db91b415253fa0dd10de169c7fa3a168",
"assets/assets/images/333_andare.png": "0e0b9e07db36d7b13766ef5cb402ecca",
"assets/assets/images/131_additivo.png": "2addb790b4342911e9f6cc0291b662b7",
"assets/assets/images/311_ammorbidente.png": "b2d6fad6893ef52bf03a2f9db01c60ff",
"assets/assets/images/256_alludere.png": "f4d23923d5b95a88dd04bf26e2e7c246",
"assets/assets/images/075_accogliente.png": "7810ee0d91465b0936b7dbae8de7d918",
"assets/assets/images/288_ambientare.png": "07fcc3c2168a7acbb40f3ff8abef9ca4",
"assets/assets/images/203_agricolo.png": "7d9f17d9fb1986f308e7a221f3b6c0f2",
"assets/assets/images/080_accompagnare.png": "3722382fc899dd2f5617d4bb9e0bbae1",
"assets/assets/images/245_allenare.png": "4c290664ae1c1b335b379e5bc5d6121a",
"assets/assets/images/133_addobbo.png": "46d841c70a13693dd415e627f1b72ce4",
"assets/assets/images/151_adescamento.png": "8117dff39a1c5561feaa7040ffc44d10",
"assets/assets/images/336_angelo.png": "7c9b81cfdb3e53e6b25ad3d1b0c9e8af",
"assets/assets/images/340_anima.png": "f95a150bc1a2c94a3a934276e817cb41",
"assets/assets/images/123_addentare.png": "572005e41edb455c06ff058d32d21f64",
"assets/assets/images/263_altamente.png": "22312df908e46b3e04efc613e711b40f",
"assets/assets/images/179_adultero.png": "9e39ee7401a3048c07b3ef3bd5d7bca1",
"assets/assets/images/251_allineare.png": "b42f523409aa8119cd289b33b7fbde1f",
"assets/assets/images/269_alterno.png": "731c801e524497e1c53e840012e6c0df",
"assets/assets/images/202_agosto.png": "7f0dc04e284b4cf57a46b87553346f56",
"assets/assets/images/067_accetta.png": "cce56bd24eedb20d43c735cc9739135c",
"assets/assets/images/144_adeguatamente.png": "8c338deff0218d95052b2f28de5c5610",
"assets/assets/images/328_anche.png": "aced07186fc474674e0a20d9391ef7d1",
"assets/assets/images/017_abbondante.png": "9e73e28c7d93967a3de26763759e7b6e",
"assets/assets/images/283_amare.png": "71562bb1f55f648235ca95868e3e9897",
"assets/assets/images/321_analisi.png": "57f25a9be3e670e17778f7e662340857",
"assets/assets/images/047_accappatoio.png": "63b6f0371c3f860755dcb1e3773f53cb",
"assets/assets/images/292_ambulanza.png": "364cd4e65ca655d0ae91a3f226bbf49b",
"assets/assets/images/135_addome.png": "b1f8080a291d77ae435640c7d634b524",
"assets/assets/images/101_acquasanta.png": "10732538d99e991b5897b05de494291d",
"assets/assets/images/085_accordo.png": "34a55293d7471355f48b74ec2ec3d19f",
"assets/assets/images/222_alga.png": "9aa34c05dcfd77811464d51248c440da",
"assets/assets/images/337_angolare.png": "cddbe64061848e61751b30731b094510",
"assets/assets/images/186_aerazione.png": "b3a67899781f181b888db5460db67940",
"assets/assets/images/243_allegro.png": "3f751de39432803df94ecef5884a8000",
"assets/assets/images/041_acca.png": "76d0c44e056282a663f870892f252167",
"assets/assets/images/224_alieno.png": "a6109a9c263f65d010ebd062f3316a55",
"assets/assets/images/059_accenno.png": "4a4346b8a9d0da0923a8cd5cc45f4a7d",
"assets/assets/images/114_acuto.png": "cc1ff918d546c778361ae14564e044c5",
"assets/assets/images/033_abituare.png": "02fa33b2ef68e57145ad53a4f93f267b",
"assets/assets/images/326_anarchico.png": "858c9ae2a928ead6a04c8461ec295ab6",
"assets/assets/images/007_abbandono.png": "f02f1aaf174295f8b9006639b002309f",
"assets/assets/images/003_abbagliante.png": "e75a34dd81290fc5dffb33adc8d5c237",
"assets/assets/images/201_agonia.png": "3151b7125b36a76dde3f2a45f8693e28",
"assets/assets/images/354_annuale.png": "99a322f1f9f874c8cb3383251db5425e",
"assets/assets/images/010_abbastanza.png": "8807673f926104607eb281152b65541c",
"assets/assets/images/330_ancora.png": "541124c7d5b1527359dddd9c763f1ca0",
"assets/assets/images/325_ananas.png": "9787ebdf9cff1d692f4113f72371403b",
"assets/assets/images/118_adattamento.png": "bfea9fcc8608afe9c3fbed0aae364a74",
"assets/assets/images/235_allarme.png": "50e5a602c966a83c72f962d41fee3934",
"assets/assets/images/073_accidente.png": "f5f87d558d81557c714cac6ab6c86934",
"assets/assets/images/014_abbinare.png": "c71358f70b73f3bad4e6f4fc5d0d2104",
"assets/assets/images/018_abbondare.png": "f64203291a58177750915179db74137c",
"assets/assets/images/092_accurato.png": "8601b325ffbf64ee5a04c5fe4354287b",
"assets/assets/images/057_accendino.png": "2b4753faddb06b648eec5887b37459da",
"assets/assets/images/338_angolo.png": "aedb17510b8e148b891fb87c06976059",
"assets/assets/images/343_animare.png": "5368f53f3e7e150bf4b8df60a8c41849",
"assets/assets/images/347_annaffiare.png": "7cec81129205f644a7dabf44ca9bfa79",
"assets/assets/images/097_acido.png": "211e0fed5a228c84b46cb371d593c81e",
"assets/assets/images/317_ampio.png": "7181a98d82919ed289460b4f3165742d",
"assets/assets/images/272_altoatesino.png": "8d77fd3076c811f8e5815d6246aae4ac",
"assets/assets/images/194_affaccendarsi.png": "9b10c4e93169f863fb73e782fbbfae3d",
"assets/assets/images/036_abortire.png": "347832f263e2c550cbcfbd07162114a3",
"assets/assets/images/072_acciaio.png": "3874ef2efc1d9aac3e0533eb46a3434e",
"assets/assets/images/334_andata.png": "0e0aec5c819776654e1c833f0983a90b",
"assets/assets/images/163_adolescenza.png": "4ed3a29ca5f6a61041e45c9f9480377a",
"assets/assets/images/016_abbonare.png": "82bbe1be32ef92bf9c660135768785ce",
"assets/assets/images/175_adulare.png": "ba983cc28511badc4c436b4a1fbcf1d3",
"assets/assets/images/219_alcol.png": "b64d33cba7c58e123fe2ddc0161d276b",
"assets/assets/images/078_accoltellare.png": "4e5b57b1e86e443e577770465aa2aeb8",
"assets/assets/images/320_analfabeta.png": "674c9d9ca9cbc65b43cf97ed79228a80",
"assets/assets/images/231_allacciare.png": "00a400dc40026aa428e35129a5ca6e39",
"assets/assets/images/102_acquavite.png": "a4bf746635ec20007c0dc06dcc1c50f3",
"assets/assets/images/166_adorabile.png": "d845e631fcbd268c92f2032da924788c",
"assets/assets/images/116_adagio.png": "16f855a59cfe3c06de0b352170a6fb42",
"assets/assets/images/030_abitazione.png": "db61092650e61ee739612b1f2a5b0989",
"assets/assets/images/063_accertare.png": "258837ca99de18859d943071359ab9db",
"assets/assets/images/327_anatra.png": "02b5b2c35c264365fb281fe93e859c30",
"assets/assets/images/274_altrettanto.png": "cbf46a5c6c8c48e1a0bbb761d47e6e4e",
"assets/assets/images/249_allevare.png": "de20e26c70a92d3329f1a0e218f96f2f",
"assets/assets/images/109_acrobata.png": "af662f51ac9896b3c5c36ba825f89114",
"assets/assets/images/188_aeronautica.png": "e1a48e4f497962c7cf6374609ff91c2d",
"assets/assets/images/352_annoiare.png": "2ca0450463678ac89b8546347c4a5ead",
"assets/assets/images/236_allattare.png": "e6dee42b08c181b33564438facae2898",
"assets/assets/images/125_addestrare.png": "983361596728871975b845bb54bb72aa",
"assets/assets/images/310_ammoniaca.png": "61884ddebc0b3dcd3c1f3b65ebe2a8d5",
"assets/assets/images/083_accorciare.png": "33b5ada39ecd6cba0d3525787054f658",
"assets/assets/images/291_ambizione.png": "65e1545a92aecd4cde9069471591b9ae",
"assets/assets/images/054_acceleratore.png": "a4b36ccb835217253fa96ad8b276c2a1",
"assets/assets/images/039_abusare.png": "554010c80908cff89b82218a5168fc00",
"assets/assets/images/159_adiposo.png": "faf5173eeecdbeb66d333634e884e7d0",
"assets/assets/images/174_adriatico.png": "a862eda40f15fe089f4c3d68699c6faf",
"assets/assets/images/154_adesivo.png": "1c68665aacb42f12e8f83dcf82e6f7dd",
"assets/assets/images/323_analizzare.png": "0d7ef1919bbcd681bea269d12c9841a1",
"assets/assets/images/346_annacquare.png": "57efff924b449844b9f461a9b7322ca3",
"assets/assets/images/225_alimentare.png": "3a2e9189f6bd4249661cc87a31b0c2a1",
"assets/assets/images/022_abbreviare.png": "ca68a62768b94c7496e5a0ecf9789acf",
"assets/assets/images/278_altrui.png": "1e5d468524703420c943bb4c42577aa0",
"assets/assets/images/148_aderente.png": "5e125754bf0d3f9f80cac24b694d4a73",
"assets/assets/images/164_adombrare.png": "8cf365b21785504beb06d4f4f4503ab8",
"assets/assets/images/261_alquanto.png": "5e636ec6ee7caa96d90e7e3857d3949d",
"assets/assets/images/250_allievo.png": "0ffc030f168caa670e24800ec456f420",
"assets/assets/images/066_accessorio.png": "12d0a62b1b44b276c062634b5a85b465",
"assets/assets/images/132_addobbare.png": "158ab7489874157c2b149b640fc080e7",
"assets/assets/images/202_affannoso.png": "b35122d52de187defb4f37d15072e7cd",
"assets/assets/images/111_acustica.png": "6aab8dd6c68819832544cca4093ebeb1",
"assets/assets/images/318_amplificatore.png": "2a8863e57877ad2816314d2b228f6f2f",
"assets/assets/images/226_alimentare_v.png": "7a01627ace36192e26120efc5bcb7a02",
"assets/assets/images/332_andamento.png": "8fc53dd4ffe68ff671ea527aa9c2968d",
"assets/assets/images/275_altrimenti.png": "25b3228b05577ae711590a2f7a86370f",
"assets/assets/images/112_acustico.png": "d9dcceb0b0451e027e901285b5786e6a",
"assets/assets/images/192_afa.png": "144c3c5801009131e7ae2a3c3cb300f5",
"assets/assets/images/279_alunno.png": "91068d7cbe8857c402ce19bc703a5e21",
"assets/assets/images/126_addetto.png": "057827eea11d95df5ec9168bfda1616a",
"assets/assets/images/255_alluce.png": "496dc318d9c777b716452f4df351b687",
"assets/assets/images/137_addormentare.png": "710e13e412def081574c6893dfaa317a",
"assets/assets/images/345_animo.png": "ecf5b1f906a1af3b35c8029cc32e79eb",
"assets/assets/images/034_abitudine.png": "62c040914e6520b8ecb4f5005aba2037",
"assets/assets/images/048_accarezzare.png": "44a3a9d25a00e29c6250a4569db1ef2e",
"assets/assets/images/217_albicocca.png": "345b1c26ddae6637c3c4c2408006a3d7",
"assets/assets/images/280_alveare.png": "16014c429b9828a16ceafce5c799e3ba",
"assets/assets/images/348_annebbiare.png": "3460617e68e9bed6aa7d580133eebad2",
"assets/assets/images/247_allentare.png": "07144f4ad084047b64ee5e782edded50",
"assets/assets/images/246_allenatore.png": "2cd37c0928a816b474f871860acc8c97",
"assets/assets/images/104_acquedotto.png": "fa90db883c3968c2568f17c67099b1e1",
"assets/assets/images/240_allegato.png": "8200106fdce894997559188888f7695b",
"assets/assets/images/200_affannarsi.png": "10a543e1807768b6ee1c5a0982f7a670",
"assets/assets/images/190_aeroporto.png": "16a163360936ff44fcaabd5178adc2da",
"assets/assets/images/050_accavallare.png": "f08d516a943e12eeeaba7d4db5c990dc",
"assets/assets/images/228_alimentazione.png": "2dec4b32bcb1777d1feabdcf66dee74c",
"assets/assets/images/259_alluvione.png": "8a6c90436ae86f80bff6df67fcecd3dd",
"assets/assets/images/149_aderenza.png": "6edcea96cb68082b6960f55783fca3df",
"assets/assets/images/096_aceto.png": "a18ee2aef99ed702c659ebf56f395c96",
"assets/assets/images/156_adiacente.png": "5c3248a38d76377dce0c34f65f0eb590",
"assets/assets/images/029_abitare.png": "377fb7080ecbcdce11b981dd97ef8a76",
"assets/assets/images/237_alleanza.png": "f65b4f178b67ce7fabf946670239bf26",
"assets/assets/images/350_anno.png": "e146e831fc0db5690e1c9d20813ddb39",
"assets/assets/images/294_amicizia.png": "8fd632637c0ebf69454f7067816f1c1a",
"assets/assets/images/120_adatto.png": "ef60b1c223178c9ebce3987c9104ca20",
"assets/assets/images/303_ammettere.png": "37d0ba368baf6162dca4094016122293",
"assets/assets/images/329_anconetano.png": "34a43062a64751b9c19d206393be47dd",
"assets/assets/images/285_amato.png": "56f4948e63b6aea1ab12904aefe2a101",
"assets/assets/images/267_alternativa.png": "5391d111a3e85e6e8b2cd9335bc29aa2",
"assets/assets/images/079_accomodare.png": "1d1e1ae13e5c464c552e7639d14ea0d9",
"assets/assets/images/307_ammirare.png": "ded2a2c7bd6e19b0b47c0afca37f0f93",
"assets/assets/images/061_accento.png": "9b44a6ba05f9f77f49bd37db08d68f9a",
"assets/assets/images/091_accumulatore.png": "0719a0d7b268cf1700efaa63bdbfec07",
"assets/assets/images/260_almeno.png": "12bc744ee9bd25816c0f7ab5ab7530a2",
"assets/assets/images/053_accelerare.png": "76c7868a58dbe8bba676c8efffbe0a8f",
"assets/assets/images/223_algerino.png": "da2261e94ce5f2d80dbf90d9dd7431dc",
"assets/assets/images/094_accusare.png": "55185e546ffdceaf54772b6d72129e31",
"assets/assets/images/230_alito.png": "16b4207820a0171f1d94b3ce30971e96",
"assets/assets/images/305_amministratore.png": "c406373c45a64302b55fb3a3de6263e4",
"assets/assets/images/147_adempimento.png": "e6b6928b4fe0bc3fd2d3cae2680732d5",
"assets/assets/images/020_abbracciare.png": "c93546f0403261e39b8baabe3e8dd7e4",
"assets/assets/images/257_alluminio.png": "600169671e58fd39c2bc59c0c7fffb08",
"assets/assets/images/195_affacciare.png": "5ef3e7bfd1b0c14fa31b202a23f2c99b",
"assets/assets/images/128_addio.png": "d00944909d3a9ec4a9ddf3ed9956a60f",
"assets/assets/images/239_alleato.png": "da3a717891667abcaf170e13463aa619",
"assets/assets/images/341_animale.png": "a1f682d48df23ad7e5a480e918a70132",
"assets/assets/images/268_alternativo.png": "8dec5aac07d14c2ee5c41cd38c19147c",
"assets/assets/images/068_accettabile.png": "54265991299e3f7840b4aa1fd4e9b87b",
"assets/assets/images/254_allora.png": "d30554b8217b8bc9f1ca1f1f474625c5",
"assets/assets/images/262_altalena.png": "79f79529412ecab676944705ca32904c",
"assets/assets/images/172_adottivo.png": "bc52e63523c5a1226636eac0e89662be",
"assets/assets/images/277_altrove.png": "191b8b39517a583f42826173e5a60eb3",
"assets/assets/images/161_adito.png": "a9f8462ae11df40c5968fb55142f73ae",
"assets/assets/images/316_ampiamente.png": "ba5acf45269b386f2313566cc07955d6",
"assets/assets/images/213_alba.png": "3378663d3641b858ec08fadb0c64ce59",
"assets/assets/images/058_accennare.png": "ef25407085be33bf9b101eba07ccef66",
"assets/assets/images/173_adozione.png": "e337591b0edd864afc8b755cb3927849",
"assets/assets/images/098_acqua.png": "12c29fd67b41f526b687c96e0cf4a926",
"assets/assets/images/178_adulterio.png": "f384da3a72bc201c07f67ab7d58ce380",
"assets/assets/images/139_addossare.png": "753cfd030d75d0483d266f2c8931925d",
"assets/assets/images/207_aguzzare.png": "8425053ea104a589058336d59780760f",
"assets/assets/images/284_amaro.png": "c90672efab094b029f19728f003c2ac4",
"assets/assets/images/028_abitante.png": "f3f0393f05f46216b0355e066257fe67",
"assets/assets/images/171_adottare.png": "d1d0ef8a1cae84c9fa93b448920128d4",
"assets/assets/images/197_affamare.png": "6a6ce4ee1676994187c7ecc0ac983818",
"assets/assets/images/206_agrume.png": "5130ddd5acb5c41d8bfaf0de7148b432",
"assets/assets/images/115_adagiare.png": "c2971d4793dcd3ed1615498d65ae6510",
"assets/assets/images/335_anello.png": "5f68bfc90f6939e70e99c4ece4d71016",
"assets/assets/images/273_altopiano.png": "022add06d56e1c7b8b211b153907b433",
"assets/assets/images/064_acceso.png": "7d3dc1fd3a6b7a4abca36e9f4f37f774",
"assets/assets/images/009_abbasso.png": "b71f7ea0184bec60ac8159bc9faea40f",
"assets/assets/images/199_affannare.png": "e77b2e286bc3173d2a00798df4361bf9",
"assets/assets/images/024_abete.png": "c83a9ecd1122d837a84f61f1db2ce29e",
"assets/assets/images/052_accedere.png": "3aae161318b414f3823eeecbcf12b289",
"assets/assets/images/011_abbattere.png": "b7986967164c0777fe1c9435e49d4683",
"assets/assets/images/157_adibire.png": "e202737f2299dcc5dd91e2b0bad00881",
"assets/assets/data/vocab_part1.json": "6e61f546752020407ac6611f1edea792",
"assets/assets/data/vocab.json": "8f5d030d0f55bd2afbc865ca550baaad",
"assets/fonts/MaterialIcons-Regular.otf": "948966080f55b94e6eb96e4e834c8e4f",
"assets/NOTICES": "44ad8f6559af3cef17e6f9f3da53f4c4",
"assets/packages/cupertino_icons/assets/CupertinoIcons.ttf": "33b7d9392238c04c131b6ce224e13711",
"assets/FontManifest.json": "dc3d03800ccca4601324923c0b1d6d57",
"assets/AssetManifest.bin": "790c694938f3ac0211992e3b81ac0dac",
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
"flutter_bootstrap.js": "6da277e1dfeddbbe6ea56bfb0f77fe49",
"version.json": "612599dc5bea04eeecf03af277de9630",
"main.dart.js": "d9756924b42980db26ab7506698bcf98"};
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
