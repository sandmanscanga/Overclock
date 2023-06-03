# Overclock - Python Package for High-Speed Processing

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

![GitHub commit activity](https://img.shields.io/github/commit-activity/w/sandmanscanga/Overclock)

![GitHub release (latest by date)](https://img.shields.io/github/v/release/sandmanscanga/Overclock?display_name=tag)
![GitHub language count](https://img.shields.io/github/languages/count/sandmanscanga/Overclock)
![GitHub top language](https://img.shields.io/github/languages/top/sandmanscanga/Overclock)

![GitHub repo size](https://img.shields.io/github/repo-size/sandmanscanga/Overclock)
![GitHub repo directory count](https://img.shields.io/github/directory-file-count/sandmanscanga/Overclock?label=directories&type=dir)
![GitHub repo directory count](https://img.shields.io/github/directory-file-count/sandmanscanga/Overclock?type=file)

![GitHub search hit counter](https://img.shields.io/github/search/sandmanscanga/Overclock/overclock)
![GitHub search hit counter](https://img.shields.io/github/search/sandmanscanga/Overclock/performance)
![GitHub search hit counter](https://img.shields.io/github/search/sandmanscanga/Overclock/threading)
![GitHub search hit counter](https://img.shields.io/github/search/sandmanscanga/Overclock/asynchronous)
![GitHub search hit counter](https://img.shields.io/github/search/sandmanscanga/Overclock/concurrency)

Overclock is an incredibly feature-rich, flexible, and user-friendly Python package designed for accelerating processes in Python. With Overclock, you can effortlessly speed up virtually any task by leveraging multi-threading capabilities.

## Features

- **Effortless Speed Boost**: Overclock allows you to easily specify the number of threads you want and provides a simple interface to process any iterable using a user-defined function for mapping.

- **Custom Thread Metrics**: Overclock includes a family of custom threads that track various metrics to provide insights into your processing. For example, the main pool's custom thread can monitor wait times, run times, average times, and total times per task. Another custom thread tracks memory management, task sizes, task results, and momentary system resource metrics.

- **Publisher Thread**: The publisher thread keeps a running index to reorganize results back into order and asynchronously populates task queues. This ensures efficient processing and orderly result management.

- **Efficient Worker Threads**: The main worker threads, which are part of the main pool, continuously listen for data from the queue and execute tasks until a kill signal is received.

## Getting Started

To start using Overclock in your Python projects, follow these steps:

1. Install Overclock via pip:

```shell
pip install overclock
```

2. Import the necessary components into your Python script:

```python
from overclock import Overclock
```

3. Specify the number of threads and pass an iterable along with a mapping function:

```python
pool = Overclock(num_threads=4)
results = pool.map(my_iterable, my_mapping_function)
```

For detailed documentation and examples, please refer to the [project repository](https://www.github.com/sandmanscanga/Overclock).

## License

Overclock is licensed under the [MIT License](https://www.github.com/sandmanscanga/Overclock/blob/main/LICENSE.md).
