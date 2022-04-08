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
    name = "sender_segmentation_deps",
    deps = [
        "//mediapipe/calculators/core:flow_limiter_calculator",
        "//mediapipe/calculators/image:recolor_calculator",
    ] + select({
        "//mediapipe/gpu:disable_gpu": [
            "//mediapipe/modules/selfie_segmentation:selfie_segmentation_cpu",
        ],
        "//conditions:default": [
            "//mediapipe/modules/selfie_segmentation:selfie_segmentation_gpu",
        ],
    }),
)

mediapipe_binary_graph(
    name = "sender_segmentation_gpu_binary_graph",
    graph = "sender_segmentation_gpu.pbtxt",
    output_name = "sender_segmentation_gpu.binarypb",
    deps = [":sender_segmentation_deps"],
)

mediapipe_binary_graph(
    name = "sender_segmentation_cpu_binary_graph",
    graph = "sender_segmentation_cpu.pbtxt",
    output_name = "sender_segmentation_cpu.binarypb",
    deps = [":sender_segmentation_deps"],
)

