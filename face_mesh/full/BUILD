# Copyright 2019 The MediaPipe Authors.
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

load(
    "//mediapipe/framework/tool:mediapipe_graph.bzl",
    "mediapipe_binary_graph",
)

licenses(["notice"])

package(default_visibility = ["//visibility:public"])

exports_files(
    srcs = glob(
        ["*.pbtxt"]
    )
)

cc_library(
    name = "playback_calculators",
    deps = [
        "//mediapipe/calculators/video:opencv_video_decoder_calculator",
        "//mediapipe/calculators/video:opencv_video_encoder_calculator",

        "//mediapipe/graphs/custom/face_mesh:facemesh_deps",
    ] + select({
        "//mediapipe/gpu:disable_gpu": [
            "//mediapipe/graphs/custom/face_mesh/full/subgraphs:face_renderer_cpu",
        ],
        "//conditions:default": [
            "//mediapipe/graphs/custom/face_mesh/full/subgraphs:face_renderer_gpu",
        ],
    }),
)

cc_library(
    name = "live_calculators",
    deps = [
        "//mediapipe/calculators/core:flow_limiter_calculator",
        "//mediapipe/calculators/custom/util:proctor_result_calculator",
        "//mediapipe/calculators/core:packet_cloner_calculator",
        "//mediapipe/graphs/custom/face_mesh:facemesh_deps",
    ] + select({
        "//mediapipe/gpu:disable_gpu": [
            "//mediapipe/graphs/custom/face_mesh/full/subgraphs:face_renderer_cpu",
        ],
        "//conditions:default": [
            "//mediapipe/graphs/custom/face_mesh/full/subgraphs:face_renderer_gpu",
        ],
    }),
)

mediapipe_binary_graph(
    name = "face_mesh_mobile_gpu_binary_graph",
    graph = "face_mesh_mobile.pbtxt",
    output_name = "face_mesh_mobile_gpu.binarypb",
    deps = [":live_calculators"],
)
