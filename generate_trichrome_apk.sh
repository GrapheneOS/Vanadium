#!/bin/bash

ANDROID_TOP=~/android/grapheneos

cd out/Default/apks

rm -f TrichromeChrome.apks
rm -f TrichromeChrome.apk

java -jar $ANDROID_TOP/prebuilts/bundletool/bundletool-all-20190905.jar build-apks --bundle TrichromeChrome.aab --output TrichromeChrome.apks --mode=universal --ks ../../../vanadium.keystore --ks-pass pass:vanadiumpass --ks-key-alias vanadiumkey
unzip TrichromeChrome.apks universal.apk
mv universal.apk TrichromeChrome.apk
