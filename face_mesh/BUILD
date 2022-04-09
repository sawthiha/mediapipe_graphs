licenses(["notice"])

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "custom_calculators",
    deps = [
        "//mediapipe/calculators/custom/util:landmark_standardization",
        "//mediapipe/calculators/custom/face_alignment:face_alignment_calculator",
        "//mediapipe/calculators/custom/eye_blink:eye_blink_calculator",
        "//mediapipe/calculators/custom/face_activity:face_movement_calculator",
    ],
)

cc_library(name = "facemesh_deps",
    deps = [
        "//mediapipe/calculators/core:constant_side_packet_calculator",
        ":custom_calculators"
    ] + select({
        "//mediapipe/gpu:disable_gpu": [
            "//mediapipe/modules/face_landmark:face_landmark_front_cpu",
        ],
        "//conditions:default": [
            "//mediapipe/modules/face_landmark:face_landmark_front_gpu",
        ],
    }),
)
