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

filegroup(name = "full_segmentation_gpu_data",
    srcs = [
        "//mediapipe/graphs/custom/segmentation/standalone:standalone_segmentation_gpu.binarypb",
        "//mediapipe/graphs/custom/segmentation/sender:sender_segmentation_gpu.binarypb",
        "//mediapipe/graphs/custom/segmentation/receiver:receiver_segmentation_gpu.binarypb",
        "//mediapipe/modules/selfie_segmentation:selfie_segmentation.tflite",
    ],
)

filegroup(name = "full_segmentation_gpu_pbtxts",
    srcs = [
        "//mediapipe/graphs/custom/segmentation/standalone:standalone_segmentation_gpu.pbtxt",
        "//mediapipe/graphs/custom/segmentation/sender:sender_segmentation_gpu.pbtxt",
        "//mediapipe/graphs/custom/segmentation/receiver:receiver_segmentation_gpu.pbtxt",
    ],
)

genrule(name = "full_segmentation_header",
    outs = ["config_header.generated.h"],
    srcs = select({
        "//mediapipe/gpu:disable_gpu": [":full_segmentation_cpu_pbtxts"],
        "//conditions:default": [":full_segmentation_gpu_pbtxts"],
    }),
    cmd = "./$(location //mediapipe/graphs/custom:graph_header_generator) $(SRCS) > $@",
    tools = ["//mediapipe/graphs/custom:graph_header_generator"],
)

cc_library(name = "full_segmentation_gpu_deps",
    deps = [
        "//mediapipe/calculators/core:flow_limiter_calculator",
        "//mediapipe/calculators/image:recolor_calculator",
        "//mediapipe/calculators/image:set_alpha_calculator",
        "//mediapipe/modules/selfie_segmentation:selfie_segmentation_gpu",
    ],
)

filegroup(name = "full_segmentation_cpu_data",
    srcs = [
        "//mediapipe/graphs/custom/segmentation/standalone:standalone_segmentation_cpu.binarypb",
        "//mediapipe/graphs/custom/segmentation/sender:sender_segmentation_cpu.binarypb",
        "//mediapipe/graphs/custom/segmentation/receiver:receiver_segmentation_cpu.binarypb",
        "//mediapipe/modules/selfie_segmentation:selfie_segmentation.tflite",
    ],
)

filegroup(name = "full_segmentation_cpu_pbtxts",
    srcs = [
        "//mediapipe/graphs/custom/segmentation/standalone:standalone_segmentation_cpu.pbtxt",
        "//mediapipe/graphs/custom/segmentation/sender:sender_segmentation_cpu.pbtxt",
        "//mediapipe/graphs/custom/segmentation/receiver:receiver_segmentation_cpu.pbtxt",
    ],
)

cc_library(name = "full_segmentation_cpu_deps",
    deps = [
        "//mediapipe/calculators/core:flow_limiter_calculator",
        "//mediapipe/calculators/image:recolor_calculator",
        "//mediapipe/calculators/image:set_alpha_calculator",
        "//mediapipe/modules/selfie_segmentation:selfie_segmentation_cpu",
    ],
)
