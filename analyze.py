import json
import matplotlib.pyplot as plt
import numpy as np
import os
import requests
import sys

width = 0.25


def plot_one_job(ax, targets, jobname, metric):
    selected = []
    for name, data in targets.items():
        selected.append((name, [job['write']
                for job in data['jobs']
                if job['jobname'] == jobname]))

    numpoints = len(selected[0][1])
    x = np.arange(numpoints)

    ax.set_title(jobname)
    for i, jobinfo in enumerate(selected):
        name, jobs = jobinfo
        if '.' in metric:
            comps = metric.split('.')
            points = [job[comps[0]][comps[1]] for job in jobs]
        else:
            points = [job[metric] for job in jobs]
        adj = (x + (width * i) - (width * (len(selected) - 1) / 2))
        r = ax.bar(adj, points, width, label=name)

        if numpoints < 4:
            ax.bar_label(r, padding=3)

    ylim = ax.get_ylim()
    ax.set_ylim(ylim[0], ylim[1] + ylim[1] * 0.8)
    ax.set_xticks(x)
    ax.legend()


targets = {}

for pv in ['nfs', 'rbd']:
    res = requests.get(f'https://benchmarks.apps.smaug.na.operate-first.cloud/results/fio-{pv}/results.json')
    targets[os.path.splitext(os.path.basename(pv))[0]] = res.json()

jobnames = set(job['jobname'] for job in list(targets.values())[0]['jobs'])

for metric in ['bw_mean', 'clat_ns.mean', 'iops', 'bw']:
    fig, axs = plt.subplots(len(jobnames))
    fig.suptitle(metric)

    for i, name in enumerate(jobnames):
        plot_one_job(axs[i], targets, name, metric)

    fig.tight_layout()
    fig.set_figwidth(8)
    fig.set_figheight(6)
    plt.savefig(f'{metric}.png')
#   plt.show()
