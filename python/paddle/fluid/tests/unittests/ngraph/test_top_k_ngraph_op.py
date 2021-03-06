# Copyright (c) 2018 PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __future__ import print_function

import unittest
from paddle.fluid.tests.unittests.test_top_k_op import TestTopkOp, TestTopkOp3d, TestTopkOp2, TestTopkOp3, TestTopkOp4


class TestNGRAPHTopkOp(TestTopkOp):
    def setUp(self):
        super(TestNGRAPHTopkOp, self).setUp()
        self._cpu_only = True


class TestNGRAPHTopkOp2(TestTopkOp2):
    def setUp(self):
        super(TestNGRAPHTopkOp2, self).setUp()
        self._cpu_only = True


class TestNGRAPHTopkOp3(TestTopkOp3):
    def setUp(self):
        super(TestNGRAPHTopkOp3, self).setUp()
        self._cpu_only = True


class TestNGRAPHTopkOp4(TestTopkOp4):
    def setUp(self):
        super(TestNGRAPHTopkOp4, self).setUp()
        self._cpu_only = True


if __name__ == "__main__":
    unittest.main()
