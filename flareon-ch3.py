# !/usr/bin/python3
import os ,re
import subprocess
import tarfile


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    START_DIR = '.'   
    OUTPUX_DIR = 'flagz2'
    nodes = []
    dir_names = [ \
        'b75ea3e81881c5d36261f64d467c7eb87cd694c85dd15df946601330f36763a4',
        'ea12384be264c32ec1db0986247a8d4b2231bf017742313c01b05a7e431d9c26',
        '4c33f90f25ea2ab1352efb77794ecc424883181cf8e6644946255738ac9f5dbd',
        '09e6fff53d6496d170aaa9bc88bd39e17c8e5c13ee9066935b089ab0312635ef',
        'e5254dec4c7d10c15e16b41994ca3cf0c5e2b2a56c9d4dc2ef053eeff24333ff',
        '7d643931f34d73776e9169551798e1c4ca3b4c37b730143e88171292dbe99264',
        '754ee87063ee108c1f939cd3a28980a03b700f3c3967df8058831edad2743fd7',
        'b5f502d32c018d6b2ee6a61f30306f9b46dad823ba503eea5b403951209fd59b',
        '81f28623cca429f9914e21790722d0351737f8ad3e823619a4f7019be72e2195',
        '76531a907cdecf03c8ac404d91cbcabd438a226161e621fab103a920600372a8',
        '6b4e128697aa0459a6caba2088f6f77efaaf29d407ec6b58939c9bc7814688ad',
        'bfefc1bdf8b980a525f58da1550b56daa67bae66b56e49b993fff139faa1472c',
        '1c5d28d6564aed0316526e8bb2d79a436b45530d2493967c8083fea2b2e518ce',
        'f9621328166de01de73b4044edb9030b3ad3d5dbc61c0b79e26f177e9123d184',
        '58da659c7d1c5a0c3447cb97cd6ffb12027c734bfba32de8b9b362475fe92fae',
        '9a31bad171ad7e8009fba41193d339271fc51f992b8d574c501cae1bfa6c3fe2',
        '49fb821d2bf6d6841ac7cf5005a6f18c4c76f417ac8a53d9e6b48154b5aa1e76',
        'fd8bf3c084c5dd42159f9654475f5861add943905d0ad1d3672f39e014757470',
        'a435765bcd8745561460979b270878a3e7c729fae46d9e878f4c2d42e5096a44',
        'cd27ad9a438a7eef05f5b5d99e2454225693e63aba29ce8553800fed23575040',
        '8e11477e79016a17e5cde00abc06523856a7db9104c0234803d30a81c50d2b71',
        'e1a9333f9eccfeae42acec6ac459b9025fe6097c065ffeefe5210867e1e2317d',
        'e6c2557dc0ff4173baee856cbc5641d5b19706ddb4368556fcdb046f36efd2e2',
        'fadf53f0ae11908b89dffc3123e662d31176b0bb047182bfec51845d1e81beb9',
        '303dfd1f7447a80322cc8a8677941da7116fbf0cea56e7d36a4f563c6f22e867',
        'f2ebdc667cbafc2725421d3c02babc957da2370fbd019a9e1993d8b0409f86dd',
        '2b363180ec5d5862b2a348db3069b51d79d4e7a277d5cf5e4afe2a54fc04730e',
        '25e171d6ac47c26159b26cd192a90d5d37e733eb16e68d3579df364908db30f2',
        'cfd7ddb31ce44bb24b373645876ac7ea372da1f3f31758f2321cc8f5b29884fb',
        'a2de31788db95838a986271665b958ac888d78559aa07e55d2a98fc3baecf6e6',
    ]

    print('Loading revisions ...')
    for i in range(len(dir_names)):

        f = os.path.join(START_DIR, dir_names[i], 'layer.tar')
        tar = tarfile.open(f, 'r')
        # tar.list()

        tar.extractall(OUTPUX_DIR)
        members = tar.getmembers()
        num_member = len(members)
        nodes.append(num_member)
        print(''.join(map(str, nodes)))
        # print(nodes)
        # print(f)

  

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
