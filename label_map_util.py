import numpy as np

def convert_label(label_map, max_num_classes, use_display_name=True):
  index_cats = np.array([1, 63, 2, 62, 3, 67,4, 82, 5, 65, 6, 72, 7, 15,8 ,18,9, 2])                                  
  max_num_classes = 90
  categories = []
  list_of_ids_already_added = []
  if not label_map:
    label_id_offset = 1
    for class_id in range(max_num_classes):
      categories.append({
          'id': class_id + label_id_offset,
          'name': 'category_{}'.format(class_id + label_id_offset)
      })
    return categories
  for item in label_map.item:
    if not 0 < item.id <= max_num_classes:
      logging.info('Ignore item %d since it falls outside of requested '
                   'label range.', item.id)
      continue
    if use_display_name and item.HasField('display_name'):
      name = item.display_name
    else:
      name = item.name
    if item.id not in list_of_ids_already_added:
      list_of_ids_already_added.append(item.id)
      categories.append({'id': index_cats[(item.id-1)*2+1], 'name': name})
  return categories
