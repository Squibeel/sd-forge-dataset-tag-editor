class DTEModifiedGallery{
    #elem;
    #items_grid;
    #items_selector;
    #current_filter = null;
    #selected_idx = -1
    #filter_idx = -1

    setElement(elem){
        this.#elem = elem;
        this.#items_grid = this.#elem.querySelectorAll('div.grid-wrap > div.grid-container > button.thumbnail-item')
        this.#items_selector = this.#elem.querySelectorAll('div.preview > div.thumbnails > button.thumbnail-item')
    }

    updateFilter(){
        if (!this.#elem) return;

        if (this.#items_grid){
            for(let i = 0; i < this.#items_grid.length; ++i){
                if(!this.#current_filter || this.#current_filter.includes(i)){
                    this.#items_grid[i].hidden = false
                }
                else{
                    this.#items_grid[i].hidden = true
                }
            }
        }
        if(this.#items_selector){
            for(let i = 0; i < this.#items_selector.length; ++i){
                if(!this.#current_filter || this.#current_filter.includes(i)){
                    this.#items_selector[i].hidden = false
                }
                else{
                    this.#items_selector[i].hidden = true
                }
            }
        }
    }

    filter(indices){
        if (!this.#elem) return;
        this.#current_filter = indices.map((e) => +e).sort((a, b) => a - b)
        this.updateFilter()
    }

    clearFilter(){
        this.#current_filter = null
        this.updateFilter()
    }

    clickCloseHandler(){
        this.#filter_idx = -1
        this.#selected_idx = -1
        this.#items_selector = null
    }
    
    addKeyHandler(callback_key_handler){
        if (!this.#elem) return;
        this.#elem.addEventListener('keydown', callback_key_handler, false)
    }

    addClickHandler(callback_clicked){
        if (!this.#elem) return;
        
        if (this.#items_grid != null) {
            this.#items_grid.forEach(function (btn) {
                if (btn) {
                    btn.addEventListener('click', callback_clicked, false);
                }
            });
        }
        if (this.#items_selector != null) {
            this.#items_selector.forEach(function (btn) {
                if (btn) {
                    btn.addEventListener('click', callback_clicked, false);
                }
            });
        }
        
    }


    addClickNextHandler(callback_clicked){
        if (!this.#elem) return;
        
        let fullImg_preview = this.#elem.querySelectorAll('div.preview > img')
        if (fullImg_preview != null) {
            fullImg_preview.forEach(function (e) {
                if (e) {
                    e.addEventListener('click', callback_clicked, false);
                }
            });
        }

    }

    addClickCloseHandler(callback_clicked){
        if (!this.#elem) return;
        
        let imgPreview_close = this.#elem.querySelectorAll('div.preview > div > button[class^="svelte"]')
        if (imgPreview_close != null) {
            imgPreview_close.forEach(function (e) {
                if (e) {
                    e.addEventListener('click', callback_clicked, false);
                }
            });
        }
        
    }

    clickClose(){
        if (!this.#elem) return;
        
        let imgPreview_close = this.#elem.querySelectorAll('div.preview > div > button[class^="svelte"]')
        if (imgPreview_close != null) {
            imgPreview_close.forEach(function (e) {
                if (e) {
                    e.click()
                }
            });
        }
        
    }

}
