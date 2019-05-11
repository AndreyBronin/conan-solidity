from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager("andreybronin")
    #builder.add_common_builds()
    builder.add(settings={"arch": "x86_64", "build_type": "Debug"}, options={"Shared", False}, env_vars={}, build_requires={})
    builder.run()
