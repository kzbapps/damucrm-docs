Как получить детализацию в Angular
=================================================
.. code-block:: javascript

    getGood (good_id) {
        this.dbQueryService.getDetail('skk_good_public',good_id)
            // .first()
            .subscribe(resp => {
                
                this.photos = [];
                
                if(resp['skk_good'] && resp['skk_good'].length > 0) {
                    this.good = resp['skk_good'][0];
                    if(this.good.file_uuid) this.photos = [this.good];
                }
                
                if(resp.skk_good_img && resp.skk_good_img.length > 0) {
                    resp.skk_good_img.forEach(photo => this.photos.push(photo));
                }
                
                this.providers = resp['prv'];
                if(this.providers && this.providers.length > 0){
                    this.provider = this.providers[0];
                }

                this.char_groups = [];
                let attrvals = resp['skk_good_attrval'] || [];

                attrvals.forEach((item) => {
                    
                    let index = this.char_groups.map(x => x.tpl_grp_id).indexOf(item.tpl_grp_id);
                    
                    if(index == -1) {
                        let group = new Models.SkkGoodGroupChar();
                        group.tpl_grp_id = item.tpl_grp_id;    
                        group.tpl_grp_id$ = item.tpl_grp_id$;    
                        group.characters.push(item);
                        this.char_groups.push(group);
                    } else {
                        this.char_groups[index].characters.push(item);
                    }
                })
                
                if(resp['skk_good_rowdsc'] && resp['skk_good_rowdsc'].length > 0) {
                    this.desc = resp['skk_good_rowdsc'];
                }
                
                if(this.photos.length > 0) {
                    this.selected_photo = this.photos[0];
                    setTimeout(() => {
                        this.native1.nativeElement.style.position = 'relative';
                        this.native1.nativeElement.style.top = '0px';
                        this.native1.nativeElement.style.height = '100%';
                    },1000)
                }
            });
    }
	
Добавим в ngAfterViewInit
	
.. code-block:: javascript

    ngAfterViewInit () {
        
        this.param_sub = this.route.queryParams.pipe(rxjs.take(1)).subscribe(params => {
            // if(!params.id) {
            //     this.router.navigate(['/pages/skkgoods']);
            //     return ;
            // }
            if(params.id) {
                this.good_id = params.id;
                this.getGood(params.id);
            }
        });
    }	