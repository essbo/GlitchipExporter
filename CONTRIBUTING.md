# Contributing

Prometheus uses GitHub to manage reviews of pull requests.

* If you have a trivial fix or improvement, go ahead and create a pull request,
  addressing (with `@...`) the maintainer of this repository (see
  [MAINTAINERS.md](MAINTAINERS.md)) in the description of the pull request.

## Collector Implementation Guidelines

The Node Exporter is not a general monitoring agent. Its sole purpose is to
expose machine metrics, as oppose to service metrics, with the only exception
being the textfile collector.

The Glitchtip Exporter is not a "general" exporter. Its purpose is to expose glitchtip
specific metrics that cannot otherwise be obtained. 

I'll try to keep the Metrics to the glitchtip API so we can keep it highly customizable.

For Linting please use the flake8 default config.