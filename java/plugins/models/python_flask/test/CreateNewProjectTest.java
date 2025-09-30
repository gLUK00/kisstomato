import org.kisstomato.plugins.models.python_flask.CreateNewProject;

public class CreateNewProjectTest {
    
    public static void main(String[] args) {
        try {
            String jsonData = "{\"projectName\":\"TestFlaskApp\", \"author\":\"Developer Test\"}";
            CreateNewProject.execute(jsonData);
            System.out.println("Test réussi !");
        } catch (Exception e) {
            System.err.println("Erreur: " + e.getMessage());
            e.printStackTrace();
        }
    }
}
