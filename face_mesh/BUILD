licenses(["notice"])

package(default_visibility = ["//visibility:public"])

cc_library(
    name = "custom_calculators",
    deps = [
        "//mediapipe/calculators/custom/util:landmark_standardization",
        "//mediapipe/calculators/custom/face_alignment:face_alignment_calculator",
        "//mediapipe/calculators/custom/eye_blink:eye_blink_calculator",
        "//mediapipe/calculators/custom/face_activity:face_movement_calculator",
        "//mediapipe/calculators/custom/face_activity:face_activity_calculator",
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

filegroup(name = "minimal_face_mesh_pbtxts",
    srcs = select({
        "//mediapipe/gpu:disable_gpu": [
            "//mediapipe/graphs/custom/face_mesh/minimal:face_mesh_cpu.pbtxt",
        ],
        "//conditions:default": [
            "//mediapipe/graphs/custom/face_mesh/minimal:face_mesh_gpu.pbtxt",
        ],
    }),
)

genrule(name = "minimal_face_mesh_header_gen",
    outs = ["config_header.generated.h"],
    srcs = [
        ":minimal_face_mesh_pbtxts",
    ],
    cmd = "./$(location //mediapipe/graphs/custom:graph_header_generator) $(SRCS) > $@",
    tools = ["//mediapipe/graphs/custom:graph_header_generator"],
)

cc_library(
  name = "minimal_face_mesh_header",
  hdrs = [":minimal_face_mesh_header_gen"],
  include_prefix = ".",
)

filegroup(name = "face_mesh_data",
    srcs = [
        "//mediapipe/modules/face_detection:face_detection_short_range.tflite",
        "//mediapipe/modules/face_landmark:face_landmark_with_attention.tflite",
    ],
)
