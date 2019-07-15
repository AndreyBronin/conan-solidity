## conan-solidity

[ ![Download](https://api.bintray.com/packages/andreybronin/conan/solidity%3Aandreybronin/images/download.svg) ](https://bintray.com/andreybronin/conan/solidity%3Aandreybronin/_latestVersion)

Conan package for [Solidity](https://github.com/ethereum/solidity).
Package depends on [boost](https://bintray.com/conan-community/conan/boost%3Aconan) and [jsoncpp](https://bintray.com/theirix/conan-repo/jsoncpp%3Atheirix) from [conan-center](https://bintray.com/conan/conan-center)

## Project setup

Add remote repo

```
conan remote add andreybronin https://api.bintray.com/conan/andreybronin/conan
```

Use in conanfile.txt


```
[requires]
Solidity/v0.5.10@andreybronin/testing

[options]
solidity:shared=True
jsoncpp:shared=True

[generators]
cmake
```
