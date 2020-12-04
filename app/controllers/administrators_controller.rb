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
            redirect_to @administrator
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
            redirect_to @administrator				
        else					
            render	'edit'				
        end
    end
    def destroy
        @administrator	=	Administrator.find(params[:id])
        @administrator.destroy
        redirect_to administrators_path
    end
end
