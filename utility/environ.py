import os


def set_environment_variables():
    os.environ['CLOUDINARY_KEY'] = '419976814271589'
    os.environ['SECRET_KEY'] = 'OLIxKOeueM-pIpOABjnBL-OvNN2Md8lB-TlKeHHJKUj-mQVlbMVT2T-0WORlcJGdu-mgZFCjrpEb-FlbKG9mIKm-nuMIBqjSup-UiFSQeavIx'
    os.environ['DATABASE_URL'] = 'postgresql://postgres:postgres@localhost:5432/zhik-store'
    os.environ['BASE_URL'] = '/api/v1/zhik/store/commerce/'
    os.environ['CLOUDINARY_SECRET'] = 'tSbI9om-kAb9aqd-Xa4hejtCSaE'
    os.environ['CLOUDINARY_NAME'] = 'zalajobi'
    os.environ['CLOUDINARY_URL'] = 'cloudinary://419976814271589:tSbI9om-kAb9aqd-Xa4hejtCSaE@zalajobi?cname=zhik-stores&upload_prefix=profile-image'
    os.environ['IMAGEKIT_URL_ENDPOINT'] = 'https://ik.imagekit.io/zalajobi/zhik-store-profile/?tr=h-300,w-300'
    os.environ['IMAGEKIT_CUSTOMER_PROFILE_BASEURL'] = 'https://ik.imagekit.io/zalajobi/zhik-store-profile/'
    os.environ['IMAGEKIT_PUBLIC_KEY'] = 'public_cMLW/yO+SwcUyNciAsBgMY8tq5E='
    os.environ['IMAGEKIT_PRIVATE_KEY'] = 'private_prDlb8HOrY9Z/mfviw2HLtd93r0='
    os.environ['DEFAULT_PROFILE_IMG'] = 'https://ik.imagekit.io/zalajobi/zhik-store/default_profile_pic_y4-z9eBo7.jpeg?ik-sdk-version=javascript-1.4.3&updatedAt=1651485516772'