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
    name = "receiver_segmentation_deps",
    deps = [
        "//mediapipe/calculators/core:flow_limiter_calculator",
        "//mediapipe/calculators/image:recolor_calculator",
        "//mediapipe/calculators/image:set_alpha_calculator",
    ],
)

mediapipe_binary_graph(
    name = "receiver_segmentation_gpu_binary_graph",
    graph = "receiver_segmentation_gpu.pbtxt",
    output_name = "receiver_segmentation_gpu.binarypb",
    deps = [":receiver_segmentation_deps"],
)

mediapipe_binary_graph(
    name = "receiver_segmentation_cpu_binary_graph",
    graph = "receiver_segmentation_cpu.pbtxt",
    output_name = "receiver_segmentation_cpu.binarypb",
    deps = [":receiver_segmentation_deps"],
)

