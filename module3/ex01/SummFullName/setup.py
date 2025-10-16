from setuptools import find_packages, setup

package_name = 'SummFullName'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ikxx',
    maintainer_email='i.grishanow@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'service_SummFullName = SummFullName.service_SummFullName_member_function:main',
            'client_SummFullName = SummFullName.client_SummFullName_member_function:main',
        ],
    },
)
