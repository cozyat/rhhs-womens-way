import com.sendgrid.*;
import com.sendgrid.helpers.mail.Mail;
import com.sendgrid.helpers.mail.objects.Content;
import com.sendgrid.helpers.mail.objects.Email;
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

public class testSendMail {
    private static final String API_KEY = "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";
    public static void sendTestEmail(String subject, String htmlContent, String senderEmail, String recipientEmail) {
        Email from = new Email(senderEmail);
        Email to = new Email(recipientEmail);
        Content content = new Content("text/html", htmlContent);
        Mail mail = new Mail(from, subject, to, content);
        SendGrid sg = new SendGrid(API_KEY);
        Request request = new Request();

        try {
            request.setMethod(Method.POST);
            request.setEndpoint("mail/send");
            request.setBody(mail.build());
            Response response = sg.api(request);
            System.out.println("Test email sent successfully to " + recipientEmail);
        } catch (IOException ex) {
            System.out.println("Failed to send test email: " + ex.getMessage());
            logError("TEST EMAIL - " + ex.getMessage());
        }
    }

    public static String readHtmlContentFromFile(String htmlFile) throws IOException {
        StringBuilder content = new StringBuilder();
        try (BufferedReader br = new BufferedReader(new FileReader(htmlFile))) {
            String line;
            while ((line = br.readLine()) != null) {
                content.append(line).append("\n");
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        return content.toString();
    }

    private static void logError(String errorMessage) {
        try (FileWriter fw = new FileWriter("womens-way-WD/error_log.txt", true);
             PrintWriter pw = new PrintWriter(fw)) {
            LocalDateTime now = LocalDateTime.now();
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");
            String formattedDateTime = now.format(formatter);
            pw.println("[" + formattedDateTime + "] " + errorMessage);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    public static void main(String[] args) throws Throwable, IOException {
        String subject = "RHHS Women's Way - October Issue";
        String htmlFile = "womens-way-WD/content.html";
        String senderEmail = "rhhswomensway@gmail.com";
        String recipientEmail = "cozyat@gmail.com";

        String htmlContent = readHtmlContentFromFile(htmlFile);
        sendTestEmail(subject, htmlContent, senderEmail, recipientEmail);
        System.exit(0);
    }
}

