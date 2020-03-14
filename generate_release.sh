#!/bin/bash

KEYSTORE=$PWD/vanadium.keystore
APKSIGNER=$PWD/third_party/android_sdk/public/build-tools/29.0.2/apksigner
BUNDLETOOL=$PWD/build/android/gyp/bundletool.py

cd out/Default/apks

rm -f TrichromeChrome.apks
rm -f TrichromeChrome.apk

$BUNDLETOOL build-apks --bundle TrichromeChrome.aab --output TrichromeChrome.apks --mode=universal --ks $KEYSTORE --ks-pass pass:vanadiumpass --ks-key-alias vanadium
unzip TrichromeChrome.apks universal.apk
mv universal.apk TrichromeChrome.apk

for app in TrichromeLibrary TrichromeWebView; do
    $APKSIGNER sign --ks $KEYSTORE --ks-pass pass:vanadiumpass --ks-key-alias vanadium $app.apk
done
