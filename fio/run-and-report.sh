#!/bin/bash

if [[ -z $TEST_NAME ]]; then
	echo "ERROR: missing required variable TEST_NAME" >&2
	exit 1
fi

fio --output=results.json --output-format=json /config/job.conf

MC_HOST_results="https://${AWS_ACCESS_KEY_ID}:${AWS_SECRET_ACCESS_KEY}@$BUCKET_HOST"
export MC_HOST_results

mc -C /tmp/config mirror --overwrite --remove /results  results/$BUCKET_NAME/results/$TEST_NAME
