# Copyright 2021 The MediaPipe Authors.
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
licenses(["notice"])

package(default_visibility = ["//visibility:public"])

cc_library(name = "full_segmentation_deps",
    deps = [
        "//mediapipe/calculators/core:flow_limiter_calculator",
        "//mediapipe/calculators/image:recolor_calculator",
        "//mediapipe/calculators/image:set_alpha_calculator",
        
    ] + select({
        "//mediapipe/gpu:disable_gpu": [
            "//mediapipe/modules/selfie_segmentation:selfie_segmentation_cpu",
        ],
        "//conditions:default": [
            "//mediapipe/modules/selfie_segmentation:selfie_segmentation_gpu",
        ],
    }),
)

filegroup(name = "full_segmentation_data",
    srcs = [
        "//mediapipe/modules/selfie_segmentation:selfie_segmentation.tflite",
    ],
)

genrule(name = "full_segmentation_header_gen",
    outs = ["config_header.generated.h"],
    srcs = [
        ":full_segmentation_pbtxts",
    ],
    cmd = "./$(location //mediapipe/graphs/custom:graph_header_generator) $(SRCS) > $@",
    tools = ["//mediapipe/graphs/custom:graph_header_generator"],
)

cc_library(
  name = "full_segmentation_header",
  hdrs = [":full_segmentation_header_gen"],
  include_prefix = ".",
)

filegroup(name = "full_segmentation_pbtxts",
    srcs = select({
        "//mediapipe/gpu:disable_gpu": [
            "//mediapipe/graphs/custom/segmentation/standalone:standalone_segmentation_cpu.pbtxt",
            "//mediapipe/graphs/custom/segmentation/sender:sender_segmentation_cpu.pbtxt",
            "//mediapipe/graphs/custom/segmentation/receiver:receiver_segmentation_cpu.pbtxt",
        ],
        "//conditions:default": [
            "//mediapipe/graphs/custom/segmentation/standalone:standalone_segmentation_gpu.pbtxt",
            "//mediapipe/graphs/custom/segmentation/sender:sender_segmentation_gpu.pbtxt",
            "//mediapipe/graphs/custom/segmentation/receiver:receiver_segmentation_gpu.pbtxt",
        ],
    }),
)
