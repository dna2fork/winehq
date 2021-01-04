ref: https://joshumax.github.io/general/2018/01/19/building-wine-3-0-on-android.html

out: https://dl.winehq.org/wine-builds/android

```
cp wine wine-native
cd wine-native
./configure --enable-win64
make

export TOOLCHAIN_TRIPLE="aarch64-linux-android"
export TOOLCHAIN_VERSION="aarch64-linux-android-4.9"

wget https://download.savannah.gnu.org/releases/freetype/freetype-2.6.tar.gz
tar xf freetype-2.6.tar.gz
cd freetype-2.6
./configure --host=$TOOLCHAIN_TRIPLE --prefix=`pwd`/output --without-zlib --with-png=no --with-harfbuzz=no
make && make install

export FREETYPE_CFLAGS="-I..."
export FREETYPE_LIBS="-L..."
./configure --host=$TOOLCHAIN_TRIPLE host_alias=$TOOLCHAIN_TRIPLE \
   --with-wine-tools=../wine-native --prefix=...
make

$NDK_ROOT/build/tools/make-standalone-toolchain.sh --platform=android-21 --install-dir=android-toolchain --toolchain=$TOOLCHAIN_VERSION
cp freetype-2.6/output/lib/libfreetype.so dlls/wineandroid.drv/assets/<arch>/lib/
cd dlls/wineandroid.drv/
make clean
make
```
