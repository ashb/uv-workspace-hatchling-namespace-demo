[![.github/workflows/demo.yaml](https://github.com/ashb/uv-workspace-hatchling-namespace-demo/actions/workflows/demo.yaml/badge.svg)](https://github.com/ashb/uv-workspace-hatchling-namespace-demo/actions/workflows/demo.yaml)

# Namespace packaging demo

This repository demonstrates using [hatchling] to generate namespace
packages that reside within a submodule of a base package,
and then how to integate that with [`uv workspace`s][uv-workspace].

The logical module is:

```
myproj  # Provided by myproj package
  myproj.submod1
  myproj.tasks
    myproj.tasks.task1  # Provided by myproj-task1 package
    myproj.tasks.task2  # Provided by myproj-task2 package
```

This repository demonstrates that these can be provided by independent packages. It does
this in a [monorepo], also demonstrating the using multiple `pyproject.toml`-defined
packages within a single repository.

See the [CI results](https://github.com/ashb/uv-workspace-hatchling-namespace-demo/actions/workflows/demo.yaml)
to verify the functionality.

[hatchling]: https://hatch.pypa.io/
[uv-workspace]: https://docs.astral.sh/uv/concepts/workspaces/
[monorepo]: https://en.wikipedia.org/wiki/Monorepo
