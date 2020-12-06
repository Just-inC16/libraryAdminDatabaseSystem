class AdministratorsController < ApplicationController
    def new
        @administrator=Administrator.new
    end
    def show 
        @administrator=Administrator.find(params[:id])
    end 
    def create 
        @administrator=Administrator.new(params.require(:administrator).permit(:title,:author,:isbn,:copies))
        if	@administrator.save 
            redirect_to '/administrators/searchPage'	
        else
            render	'new'
        end
    end
    def index 
        @administrators=Administrator.all
   end
    def edit
        @administrator	=Administrator.find(params[:id])
    end
    def update
        @administrator	=	Administrator.find(params[:id])				
        if	@administrator.update(params.require(:administrator).permit(:title,:author,:isbn,:copies))						
            redirect_to '/administrators/searchPage'				
        else					
            render	'edit'				
        end
    end
    def destroy
        @administrator	=	Administrator.find(params[:id])
        @administrator.destroy
        redirect_to administrators_path
    end
    def search
        #Check title 
        if (params[:title].present?)
            titleCase=params[:title]
        else    
            titleCase="%" +params[:title] +"%"    
        end
         #Check author 
         if (params[:author].present?)
            authorCase=params[:author]
        else    
            authorCase="%" +params[:author] +"%"    
        end
         #Check isbn 
         if (params[:isbn].present?)
            isbnCase=params[:isbn]
        else    
            isbnCase="%" +params[:isbn] +"%"    
        end
        @administrators = Administrator.where("title LIKE ? AND author LIKE ? AND isbn LIKE ?",titleCase, authorCase, isbnCase)
    end
    def searchPage
        @administrators=Administrator.all
    end
    def checkoutBook
        administrator = Administrator.find(params[:admin])
        if (administrator.copies==0)
            # render search_path, danger:"This book can not be checkout!"
        else
            administrator.update_attribute(:copies, administrator.copies-1)
            redirect_to '/administrators/searchPage'
        end
    end
end
