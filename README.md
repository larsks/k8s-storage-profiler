# Storage performance testing

1. Run two [fio][] jobs:

    - one against a NFS PV
    - one against a Ceph RBD PV

2. Collect the output of `fio` in a bucket

3. Expose that bucket via http

Run the `analyze.py` script locally to create visualizations of the
data.

The benchmarks are the ones [recommended by Ars
Technica][bench].

[bench]: https://arstechnica.com/gadgets/2020/02/how-fast-are-your-disks-find-out-the-open-source-way-with-fio/
[fio]: https://fio.readthedocs.io/en/latest/fio_doc.html
