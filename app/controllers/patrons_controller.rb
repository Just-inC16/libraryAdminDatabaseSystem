class PatronsController < ApplicationController
    def create
        @administrator	=	Administrator.find(params[:administrator_id])
        @patron	=	@administrator.patrons.create(params.require(:patron).permit(:name,	:review))
        redirect_to administrator_path(@administrator)
    end
    def destroy
        @administrator	=	Administrator.find(params[:administrator_id])
        @patron	=	@administrator.patrons.find(params[:id])
        @patron.destroy
        redirect_to administrator_path(@administrator)
    end 
    def show 
        @administrator=Administrator.find(params[:administrator_id])
    end 
    def index 
    end
    def searchForPatron
        #Check title 
        if (params[:titleP].present?)
            titleCase=params[:titleP]
        else    
            titleCase="%" +params[:titleP] +"%"    
        end
         #Check author 
         if (params[:authorP].present?)
            authorCase=params[:authorP]
        else    
            authorCase="%" +params[:authorP] +"%"    
        end
         #Check isbn 
         if (params[:isbnP].present?)
            isbnCase=params[:isbnP]
        else    
            isbnCase="%" +params[:isbnP] +"%"    
        end
        @administrators = Administrator.where("title LIKE ? AND author LIKE ? AND isbn LIKE ?",titleCase, authorCase, isbnCase)
    end
    def new
        @administrator=Administrator.find(params[:administrator_id])
    end
   
end
