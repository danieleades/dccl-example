#!python3

import subprocess
from pathlib import Path

PACKAGE_NAME = "sb_dccl"

PROTO_SOURCE = (Path.cwd() / ".." / "proto").resolve()
PROTO_OUTPUT = Path.cwd() / "src" / PACKAGE_NAME
DCCL_INCLUDE = (Path.cwd() / ".." / ".." / "dccl" / "dccl" / "include").resolve()


def create_directory():
    print(f"creating output directory: {PROTO_OUTPUT}")
    PROTO_OUTPUT.mkdir(parents=True, exist_ok=True)


def code_generation():
    print("running code-generation")

    protofiles = [str(path) for path in PROTO_SOURCE.glob("**/*.proto")]

    print("found proto files:")
    for file in protofiles:
        print(f"  {file}")

    command = [
        "protoc",
        f"--python_out={PROTO_OUTPUT}",
        "-I",
        "/usr/include",
        "-I",
        DCCL_INCLUDE,
        f"-I{PROTO_SOURCE}",
    ] + protofiles

    subprocess.run(command)


def run():
    print("running..")
    create_directory()
    code_generation()


if __name__ == "__main__":
    run()
