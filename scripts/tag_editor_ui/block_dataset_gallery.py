from __future__ import annotations
from typing import TYPE_CHECKING, Callable, List

import gradio as gr

from .ui_common import *
from .uibase import UIBase

if TYPE_CHECKING:
    from .ui_classes import *

class DatasetGalleryUI(UIBase):
    def __init__(self):
        self.selected_path = ''
        self.selected_index = -1
        self.selected_index_prev = -1

    def create_ui(self, image_columns):
        with gr.Row(visible=False):
            self.cbg_hidden_dataset_filter = gr.CheckboxGroup(label='Dataset Filter')
            self.nb_hidden_dataset_filter_apply = gr.Number(label='Filter Apply', value=-1)
            self.nb_hidden_image_index = gr.Number(value=None, label='hidden_idx_next')
            self.nb_hidden_image_index_prev = gr.Number(value=None, label='hidden_idx_prev')
        self.gl_dataset_images = gr.Gallery(label='Dataset Images', elem_id="dataset_tag_editor_dataset_gallery", columns=image_columns)
    
    def set_callbacks(self, load_dataset:LoadDatasetUI, gallery_state:GalleryStateUI, get_filters:Callable[[], dte_module.filters.Filter]):
        gallery_state.register_value('Selected Image', self.selected_path)

        load_dataset.btn_load_datasets.click(
            fn=lambda:[-1, -1],
            outputs=[self.nb_hidden_image_index, self.nb_hidden_image_index_prev]
        )

        self.nb_hidden_image_index.change(
            fn=self.func_to_set_value('selected_index', int),
            inputs=self.nb_hidden_image_index
        )
        self.nb_hidden_image_index_prev.change(
            fn=self.func_to_set_value('selected_index_prev', int),
            inputs=self.nb_hidden_image_index_prev
        )
        
        self.nb_hidden_dataset_filter_apply.change(
            fn=lambda a, b: [a, b],
            _js='(x, y) => [y>=0 ? dataset_tag_editor_gl_dataset_images_filter(x) : x, -1]',
            inputs=[self.cbg_hidden_dataset_filter, self.nb_hidden_dataset_filter_apply],
            outputs=[self.cbg_hidden_dataset_filter, self.nb_hidden_dataset_filter_apply]
        )

        self.gl_dataset_images.select(
            fn=self.on_gallery_select,
            inputs=None,
            outputs=[self.nb_hidden_image_index]
        )
   
    def on_gallery_select(self, evt: gr.SelectData):
        selected_index = evt.index if evt else -1
        self.selected_index = selected_index
        return selected_index
