from setuptools import setup, find_packages

setup(name='instana',
      version='0.6.3',
      download_url='https://github.com/instana/python-sensor',
      url='https://www.instana.com/',
      license='MIT',
      author='Instana Inc.',
      author_email='peter.lombardo@instana.com',
      description='Metrics sensor and trace collector for Instana',
      packages=find_packages(exclude=['tests', 'examples']),
      long_description="The instana package provides Python metrics and traces for Instana.",
      zip_safe=False,
      setup_requires=['nose>=1.0'],
      install_requires=['autowrapt>=1.0',
                        'fysom>=2.1.2',
                        'opentracing>=1.2.1,<1.3',
                        'basictracer>=2.2.0',
                        'psutil>=5.1.3'],
      entry_points={'django': ['django.core.handlers.base = instana.django:hook'],
                    'django19': ['django.core.handlers.base = instana.django19:hook'],
                    'flask': ['flask = instana.flaskana:hook'],
                    'runtime': ['string = instana.runtime:hook']},
      test_suite='nose.collector',
      keywords=['performance', 'opentracing', 'metrics', 'monitoring'],
      classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: System :: Monitoring',
        'Topic :: System :: Networking :: Monitoring',
        'Topic :: Software Development :: Libraries :: Python Modules'])
