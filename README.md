# Metrics Submission
[![Build Status](https://travis-ci.org/hirmeos/metrics_submission.svg?branch=master)](https://travis-ci.org/hirmeos/metrics_submission) [![Release](https://img.shields.io/github/release/hirmeos/metrics_submission.svg?colorB=58839b)](https://github.com/hirmeos/metrics_submission/releases) [![License](https://img.shields.io/github/license/hirmeos/metrics_submission.svg?colorB=ff0000)](https://github.com/hirmeos/metrics_submission/blob/master/LICENSE)

Read HIRMEOS-normalised metrics from CSV files and submit them to a [metrics API][1]. You must have produced these CSVs first, using either one of the [HIRMEOS drivers][2] or your custom code.

## Setup
## Run via crontab
```
0 0 * * 0 docker run --rm --name "metrics_submission" --env-file /path/to/config.env -v metrics:/usr/src/app/metrics:ro openbookpublishers/metrics_submission:1
```

[1]: https://github.com/hirmeos/metrics-api "Metrics API"
[2]: https://metrics.operas-eu.org/docs/getting-started "Metrics docs"
