#!/bin/bash
export IAM_TOKEN=`yc iam create-token`
echo 'key= ' IAM_TOKEN >test.key