import streamlit as st  # type: ignore
from services.blob_service import upload_blob  # type: ignore


def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada", use_column_width=True)
    st.write("Validação de informações de cartão de crédito:")

    if credit_card_info and credit_card_info.get("card_name"):
        st.markdown(
            f"<h3 style='color:green;'>Nome no Cartão: {credit_card_info['card_name']}</h3>",
            unsafe_allow_html=True,
        )
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Data de Validade: {credit_card_info.get('expiry_date', 'N/A')}")
        st.write(f"Banco Emissor: {credit_card_info.get('bank_name', 'N/A')}")
        st.write(f"Bandeira: {credit_card_info.get('card_brand', 'N/A')}")
        st.write(f"Número do Cartão: {credit_card_info.get('card_number', 'N/A')}")
    else:
        st.markdown(
            "<h3 style='color:red;'>Cartão de crédito inválido.</h3>",
            unsafe_allow_html=True,
        )
        st.write("Nenhuma informação válida foi detectada.")


def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio Azure - Fake Docs")

    uploaded_file = st.file_uploader(
        "Escolha um arquivo PDF ou Imagem", type=["pdf", "png", "jpeg", "jpg"]
    )

    # Se o usuário enviou um arquivo
    if uploaded_file is not None:
        file_name = uploaded_file.name

        # Envia para o Azure Blob Storage
        blob_url = upload_blob(uploaded_file, file_name)

        if blob_url:
            st.success(
                f"Arquivo **{file_name}** enviado com sucesso para o Azure Blob Storage!"
            )

            # Ainda não implementado → deixei como vazio
            credit_card_info = {}

            show_image_and_validation(blob_url, credit_card_info)

        else:
            st.error(
                f"Erro ao enviar o arquivo **{file_name}** para o Azure Blob Storage."
            )


if __name__ == "__main__":
    configure_interface()
