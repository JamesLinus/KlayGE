################################################
# !!!! DO NOT DELETE ANY FIELD OF THIS FILE !!!!
################################################

# Compiler name.
#   On Windows desktop, could be "vc141", "vc140", "mingw", "auto".
#   On Windows store, could be "vc141", "vc140", "auto".
#   On Windows phone, could be "vc141", "vc140", "auto".
#   On Android, could be "clang", "auto".
#   On Linux, could be "gcc", "auto".
#   On MacOSX, could be "clang", "auto".
#   On iOS, could be "clang", "auto".
compiler		= "auto"

# Toolset name.
#   On Windows desktop, could be "vc141", "v140", "auto".
#   On Windows store, could be "auto".
#   On Windows phone, could be "auto".
#   On Android, could be "auto".
#   On Linux, could be "auto".
#   On MacOSX, could be "auto".
#   On iOS, could be "auto".
toolset			= "auto"

# Target CPU architecture.
#   On Windows desktop, could be "x86", "x64".
#   On Windows store, could be "arm", "x86", "x64".
#   On Windows phone, could be "arm", "x86".
#   On Android, cound be "armeabi", "armeabi-v7a", "arm64-v8a", "x86", "x86_64".
#   On Linux, could be "x86", "x64".
#   On MacOSX, could be "x64".
#   On iOS, could be "arm", "x86".
arch			= ("x64", )

# Configuration. Could be "Debug", "Release", "MinSizeRel", "RelWithDebInfo".
config			= ("Debug", "RelWithDebInfo")

# Target platform for cross compiling. Could be "android" plus version number, "win_store", "win_phone" plus version number, "ios", or "auto".
target			= "auto"

# A name for offline FXML compiling. Could be one of "d3d_11_0", "d3d_10_1", "d3d_10_0", "d3d_9_3", "d3d_9_1", "gles_2_0", "gles_3_0", "gles_3_1", "gles_3_2", or "auto".
shader_platform_name	= "auto"
