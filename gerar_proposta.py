from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def criar_pdf():
    doc = SimpleDocTemplate("Proposta_Frigo_Frutas.pdf", pagesize=letter,
                            rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    styles = getSampleStyleSheet()

    # Estilos Customizados
    titulo_style = ParagraphStyle(
        'Titulo',
        parent=styles['Heading1'],
        fontSize=20,
        textColor=colors.HexColor('#00875A'),
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )
    
    subtitulo_style = ParagraphStyle(
        'Subtitulo',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#555555'),
        spaceAfter=20
    )

    h2_style = ParagraphStyle(
        'H2',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#005c3d'),
        spaceBefore=15,
        spaceAfter=10,
        fontName='Helvetica-Bold'
    )

    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        textColor=colors.HexColor('#333333'),
        spaceAfter=8
    )

    # Cabecalho
    story.append(Paragraph("Proposta Comercial: Sistema Digital Frigo Frutas", titulo_style))
    story.append(Paragraph("Desenvolvido para Frigo Frutas • Patos/PB | Silva Apps Lab", subtitulo_style))
    story.append(Spacer(1, 10))

    # Resumo
    story.append(Paragraph("1. Visão Geral da Solução", h2_style))
    story.append(Paragraph("Apresentamos a solução digital completa desenvolvida exclusivamente para o <b>Frigo Frutas</b> em Patos/PB, composta por um Aplicativo PWA moderno, um Site Institucional e um Painel Administrativo de Gestão.", body_style))
    story.append(Paragraph("• <b>Aplicativo PWA:</b> Pedidos instantâneos, catálogo inteligente, cálculo de frete por bairro em Patos e checkout para WhatsApp.<br/>• <b>Painel Administrativo Privado:</b> Gestão de produtos, ofertas e estoque protegida por login e senha.<br/>• <b>Site Institucional:</b> Presença digital e instruções de uso.", body_style))

    # Tabela Financeira
    story.append(Spacer(1, 10))
    story.append(Paragraph("2. Investimento e Condições", h2_style))

    dados_tabela = [
        ['Item / Serviço', 'Descrição', 'Valor'],
        ['Implementação (Setup)', 'App PWA + Site + Painel Admin + Banco de Dados', 'R$ 1.500,00'],
        ['Suporte & Hospedagem', 'Servidores no ar, manutenção contínua e backups', 'R$ 200,00 /mês']
    ]

    tabela = Table(dados_tabela, colWidths=[150, 260, 120])
    tabela.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#00875A')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 8),
        ('BACKGROUND', (0, 1), (-1, -1), colors.HexColor('#F9FAFB')),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#E5E7EB')),
        ('ALIGN', (2, 0), (2, -1), 'RIGHT'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
    ]))
    
    story.append(tabela)

    # Beneficios
    story.append(Spacer(1, 10))
    story.append(Paragraph("3. Principais Diferenciais para o Negócio", h2_style))
    story.append(Paragraph("✓ <b>Zero Comissões:</b> 100% do valor das vendas fica na loja (diferente de marketplaces que cobram até 30%).<br/>✓ <b>Agilidade:</b> O cliente monta o pedido em segundos e envia direto no WhatsApp da loja.<br/>✓ <b>Autonomia Total:</b> Altere preços e crie ofertas no seu celular a qualquer momento.", body_style))

    doc.build(story)
    print("PDF 'Proposta_Frigo_Frutas.pdf' gerado com sucesso!")

if __name__ == '__main__':
    criar_pdf()
