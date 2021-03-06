# Copyright 2021 The Kubeflow Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import kfp
from .metrics_visualization_v2 import metrics_visualization_pipeline
from .util import run_pipeline_func, TestCase


def verify(run, run_id: str, **kwargs):
    assert run.status == 'Succeeded'


run_pipeline_func([
    TestCase(pipeline_func=metrics_visualization_pipeline, verify_func=verify,  mode=kfp.dsl.PipelineExecutionMode.V2_COMPATIBLE),
])