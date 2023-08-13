#!/usr/bin/env python
from setuptools import dist

dist.Distribution().fetch_build_eggs(["setuptools_rust"])
from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="deadbear-fib-rs",
    version="0.1",
    rust_extensions=[
        RustExtension(
            ".deadbear_fib_rs.deadbear_fib_rs", path="Cargo.toml", binding=Binding.PyO3
        )
    ],
    packages=["deadbear_fib_rs"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Rust",
        "Operating System :: POSIX",
        "Operating System :: MacOS :: MacOS X",
    ],
    entry_points={
        "console_scripts": [
            "fib-number = deadbear_fib_rs.fib_number_command:fib_number_command",
        ],
    },
    zip_safe=False,
)
