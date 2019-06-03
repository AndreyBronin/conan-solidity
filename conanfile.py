from conans import ConanFile, CMake, tools


class SolidityConan(ConanFile):
    name = "solidity"
    version = "v0.5.9"
    license = "GPL-3.0"
    author = "Andrey Bronin <jonnib@jandex.ru>"
    url = "https://github.com/AndreyBronin/conan-solidity"
    description = "Conan package for solidity"
    topics = ("solidity", "etherium")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=True"
    generators = "cmake"
    requires = (
        "boost/1.70.0@conan/stable",
        "jsoncpp/1.8.4@theirix/stable"
        )

    def source(self):
        git = tools.Git(folder=self.name)
        git.clone(str("https://github.com/ethereum/solidity"), self.version)

        tools.replace_in_file("solidity/CMakeLists.txt", "project(solidity VERSION ${PROJECT_VERSION} LANGUAGES CXX)",
                              '''project(solidity VERSION ${PROJECT_VERSION} LANGUAGES CXX)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

        tools.replace_in_file("solidity/CMakeLists.txt", "include(jsoncpp)", "")
        tools.replace_in_file("solidity/cmake/EthCompilerSettings.cmake", "add_compile_options(-stdlib=libstdc++)", "")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder=self.name, defs = {"USE_CVC4": "OFF", "USE_Z3": "OFF"})
        cmake.build()

    def package(self):
        # self.copy("*.h", dst="include", src="solidity")
        self.copy("*.h", dst="include/libsolidity/interface", src="solidity/libsolidity/interface")
        self.copy("*.h", dst="include/libevmasm", src="solidity/libevmasm")
        self.copy("*.h", dst="include/libdevcore", src="solidity/libdevcore")
        self.copy("*.h", dst="include/liblangutil", src="solidity/liblangutil")


        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        # self.cpp_info.libs = ["solidity"]
        self.cpp_info.libs = ["devcore", "evmasm",  "langutil",  "solc",  "solidity",  "yul",  "yulInterpreter"]
