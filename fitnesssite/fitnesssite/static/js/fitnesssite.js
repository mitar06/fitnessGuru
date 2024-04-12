document.addEventListener('alpine:init', () => {
    Alpine.data('blogProgress', () => ({
        open: false,
        progress : 0,
        showProgress: false,
        blogBodyElement : undefined ,

        init(){
            this.blogBodyElement = document.getElementById('blogBody');
        },
        resetProgress(){
            this.showProgress = false;
            this.progress = 0;
        },
        updateProgress(){
            if (!this.showProgress && this.blogBodyElement){
                this.showProgress = true;
            }
            let winHeight = window.innerHeight;
            let postBody = this.blogBodyElement;
            let postContentHeight = postBody.offsetHeight;          
            let postContentStartPosition = postBody.offsetTop;
            let winScrollTop = window.scrollY;
            let postScrollTop = postContentStartPosition - winScrollTop;
            let postScrollableArea = postContentHeight - winHeight;
            let postScrollPercentage = Math.abs((postScrollTop/postScrollableArea)*100);
            
            if (winScrollTop <= 50){
                /** Handling the height of the navbar element */
                this.resetProgress();
                return;
            }
            this.progress = postScrollPercentage;
        }
    }))
})