licenses(["notice"])

package(default_visibility = ["//visibility:public"])

exports_files(
    srcs = glob(
        ["*.pbtxt"]
    )
)

cc_library(
    name = "live_calculators",
    deps = [
        "//mediapipe/calculators/custom/util:proctor_result_calculator",
        "//mediapipe/calculators/custom/util:proctor_result",
        "//mediapipe/calculators/core:flow_limiter_calculator",
        "//mediapipe/graphs/custom/face_mesh:facemesh_deps",
    ],
)
