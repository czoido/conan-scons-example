import os

from conan import ConanFile
from conan.tools.files import copy


class helloConan(ConanFile):
    name = "hello"
    version = "1.0"
    settings = "os", "compiler", "build_type", "arch"

    exports_sources = "src/*"

    # TODO: check what would be the correct layout and how to interact with
    # SCons scripts
    def layout(self):
        self.folders.source = "src"

    def build(self):
        debug_opt = '--debug-build' if self.settings.build_type == 'Debug' else ''
        self.run(f'scons -C {self.folders.source} {debug_opt}')

    def package(self):
        copy(self, pattern="*.h", dst=os.path.join(self.package_folder, "include"), src=os.path.join(self.source_folder),)
        copy(self, "*.lib", src=self.source_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)
        copy(self, "*.a", src=self.source_folder, dst=os.path.join(self.package_folder, "lib"), keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["hello"]

