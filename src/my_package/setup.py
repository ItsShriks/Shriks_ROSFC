from setuptools import find_packages, setup

package_name = 'my_package'

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
    maintainer='shrikar',
    maintainer_email='nakhyeshrikar@icloud.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points=
    {
        'console_scripts': 
        [
            #"<EXC_NAME> = <PACK_NAME>,<MODULE>:<METHOD>"
            #Node Name = Package Name.File name without extension:Function"
            "base_node = my_package.Base:main",
            "logger_node = my_package.logger:main",
            "hello = my_package.Pub:main",
            "my_subscribe = my_package.Sub:main",
            "my_counter = my_package.Counter:main",
            "my_increment = my_package.Increment:main"

        ],
    },
)
