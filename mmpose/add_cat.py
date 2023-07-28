import json
scene = ['Entertainment', 'ConductMusic', 'Online_class', 
         'TalkShow', 'Speech', 'Fitness', 'Interview', 'Olympic', 'TVShow', 
         'Singing', 'SignLanguage', 'Movie', 'LiveVlog', 'VideoConference']
for key in scene:
    with open('data/UBody/annotations/'+key+'/keypoint_annotation.json', 'r',encoding='utf-8') as fl:
        lines = fl.readlines()
        cat=json.loads(lines[0])
        cat['categories'] = [
                {
                    "supercategory": "person",
                    "id": 1,
                    "name": "person",
                    "keypoints": [
                        "nose",
                        "left_eye",
                        "right_eye",
                        "left_ear",
                        "right_ear",
                        "left_shoulder",
                        "right_shoulder",
                        "left_elbow",
                        "right_elbow",
                        "left_wrist",
                        "right_wrist",
                        "left_hip",
                        "right_hip",
                        "left_knee",
                        "right_knee",
                        "left_ankle",
                        "right_ankle"
                    ],
                    "skeleton": [
                        [
                            16,
                            14
                        ],
                        [
                            14,
                            12
                        ],
                        [
                            17,
                            15
                        ],
                        [
                            15,
                            13
                        ],
                        [
                            12,
                            13
                        ],
                        [
                            6,
                            12
                        ],
                        [
                            7,
                            13
                        ],
                        [
                            6,
                            7
                        ],
                        [
                            6,
                            8
                        ],
                        [
                            7,
                            9
                        ],
                        [
                            8,
                            10
                        ],
                        [
                            9,
                            11
                        ],
                        [
                            2,
                            3
                        ],
                        [
                            1,
                            2
                        ],
                        [
                            1,
                            3
                        ],
                        [
                            2,
                            4
                        ],
                        [
                            3,
                            5
                        ],
                        [
                            4,
                            6
                        ],
                        [
                            5,
                            7
                        ]
                    ]
                }
            ]

    with open('data/UBody/annotations/'+key+'/keypoint_annotation.json', 'w',encoding='utf-8') as fp:
        json.dump(cat, fp, ensure_ascii=False)