# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import os
import os.path


class OrganizationJsonWriterPipeline(object):
    """
    Save data of each item to its own JSON file.
    """

    def _create_directory_if_not_exists(self, dirname):
        if not os.path.exists(dirname):
            os.mkdir(dirname)

    def _get_full_path(self, filename, dirname):
        self._create_directory_if_not_exists(dirname)
        return os.path.join(dirname, filename)

    def _save_item_to_the_file(self, item, filename, dirname=None):
        fullpath = self._get_full_path(filename, dirname) \
            if dirname is not None else filename

        with open(fullpath, 'w') as file_handler:
            data = json.dumps(dict(item), ensure_ascii=False)
            file_handler.write(data)

    def process_item(self, item, spider):
        self._save_item_to_the_file(
            item=item,
            filename='{}.json'.format(item['name']),
            dirname='output')

        return item
