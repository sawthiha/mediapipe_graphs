load(
    "//mediapipe/framework/tool:mediapipe_graph.bzl",
    "mediapipe_binary_graph",
)

licenses(["notice"])

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "standalone_segmentation_gpu_deps",
    deps = [
        "//mediapipe/calculators/core:flow_limiter_calculator",
        "//mediapipe/calculators/image:set_alpha_calculator",
        "//mediapipe/modules/selfie_segmentation:selfie_segmentation_gpu",
    ],
)

mediapipe_binary_graph(
    name = "stanalone_segmentation_gpu_binary_graph",
    graph = "standalone_segmentation_gpu.pbtxt",
    output_name = "standalone_segmentation_gpu.binarypb",
    deps = [":standalone_segmentation_gpu_deps"],
)

cc_library(
    name = "standalone_segmentation_cpu_deps",
    deps = [
        "//mediapipe/calculators/core:flow_limiter_calculator",
        "//mediapipe/calculators/image:recolor_calculator",
        "//mediapipe/modules/selfie_segmentation:selfie_segmentation_cpu",
    ],
)

mediapipe_binary_graph(
    name = "standalone_segmentation_cpu_binary_graph",
    graph = "standalone_segmentation_cpu.pbtxt",
    output_name = "standalone_segmentation_cpu.binarypb",
    deps = [":standalone_segmentation_cpu_deps"],
)

