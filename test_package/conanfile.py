import os

from conan import ConanFile

class helloTestConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "SConsDeps"
    apply_env = False
    test_type = "explicit"

    def requirements(self):
        self.requires(self.tested_reference_str)

    def build(self):
        debug_opt = '--debug-build' if self.settings.build_type == 'Debug' else ''
        self.run(f'scons {debug_opt}')

    # TODO: check how to setup layout and scons
    def layout(self):
        self.folders.source = "."
        self.folders.generators = self.folders.source
        self.cpp.build.bindirs = ["build"]

    def test(self):
        cmd = os.path.join(self.cpp.build.bindirs[0], "main")
        self.run(cmd, env="conanrun")
